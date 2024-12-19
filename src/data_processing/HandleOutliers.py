from src.main.SmartphonesDataset import SmartphonesDataset
from scipy.stats import zscore
import pandas as pd


class HandleOutliers:
    def __init__(self):
        self.smartphones_instance = SmartphonesDataset()
        self.df = self.smartphones_instance.get_dataframe()
        self.numerical_features = self.smartphones_instance.numerical_attributes

    def check_negative_values(self):
        for col in self.numerical_features:
            # Check for negative values in the column
            negative_values = self.df[self.df[col] < 0]

            # If there are negative values, print the column and the rows with negative values
            if not negative_values.empty:
                print(f"Negative values found in column '{col}':")
                print(negative_values[[col]])  # Display only the negative values
            else:
                print(f"No negative values in column '{col}'.")

    def check_non_numeric_values(self):
        for col in self.numerical_features:
            # Check for non-numeric values (excluding nulls as they are handled later)
            non_numeric = self.df[~self.df[col].isnull() & ~pd.to_numeric(self.df[col], errors='coerce').notnull()]

            # If non-numeric values are found, print the column and the rows
            if not non_numeric.empty:
                print(f"Non-numeric values found in column '{col}':")
                print(non_numeric[[col]])
            else:
                print(f"No non-numeric values in column '{col}'.")

    def get_outliers(self):
        col = 'price'
        z_scores = self.df[[col]].apply(zscore)
        outliers = (z_scores > 5) | (z_scores < -5)
        # Filter rows where at least one column has True value
        rows_with_outliers = outliers[outliers[col]]

        print(self.df[col].min(), self.df[col].max(), self.df[col].mean())
        # Print the filtered rows
        print(rows_with_outliers)

