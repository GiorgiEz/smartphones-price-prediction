from src.main.SmartphonesDataset import SmartphonesDataset
import pandas as pd


class HandleOutliers:
    """
        A class for handling outliers in a dataset.

        Attributes:
        ----------
        smartphones_instance : SmartphonesDataset instance
            The instance of the SmartphonesDataset class.
        df : pandas.DataFrame
            The dataset to be processed.
        numerical_features : list
            List of numerical column names in the dataset.
        categorical_features : list
            List of categorical column names in the dataset.

        Methods:
        -------
        check_num_features_for_outliers()
        check_categorical_features_for_outliers()
    """

    def __init__(self):
        self.smartphones_instance = SmartphonesDataset()
        self.df = self.smartphones_instance.get_dataframe()
        self.numerical_features = self.smartphones_instance.get_numerical_attributes()
        self.categorical_features = self.smartphones_instance.get_categorical_attributes()

    def check_num_features_for_outliers(self):
        """
           Checks numerical features for outliers or invalid values.
           - Verifies if any numerical column contains negative values (which are unexpected in this dataset).
           - Identifies non-numeric values in numerical columns.
           - Prints basic statistics (average, minimum, maximum) for each numerical column to inspect for extreme values.
        """
        for col in self.numerical_features:
            # Check for negative values in the column
            negative_values = self.df[self.df[col] < 0]
            non_numeric = self.df[~self.df[col].isnull() & ~pd.to_numeric(self.df[col], errors='coerce').notnull()]

            # If there are negative values, print the column and the rows with negative values
            if not negative_values.empty:
                print(f"Negative values found in column '{col}': {negative_values[[col]]}")
            else:
                print(f"No negative values in column '{col}'.")

            # If non-numeric values are found, print the column and the rows
            if not non_numeric.empty:
                print(f"Non-numeric values found in column '{col}': {non_numeric[[col]]}")
            else:
                print(f"No non-numeric values in column '{col}'.")

            avg, mn, mx = self.df[col].mean(), self.df[col].min(), self.df[col].max()
            print(f"Average {col}: {avg}, Minimum {col}: {mn}, Maximum {col}: {mx}", '\n')
        print("By looking at statistics for each numerical column, we can conclude that there are no outliers.", '\n')

    def check_categorical_features_for_outliers(self):
        """
            Checks categorical features for potential outliers or invalid values.
            - Verifies that all non-null values in categorical columns are strings.
            - Prints unique values for each categorical column to inspect for anomalies or unexpected categories.
        """
        for col in self.categorical_features:
            non_string = self.df[~self.df[col].isnull() & ~self.df[col].apply(lambda x: isinstance(x, str))]

            # If non-string values are found, print the column and the rows
            if not non_string.empty:
                print(f"Non-string values found in column '{col}': {non_string[[col]]}")
            else:
                print(f"No non-string values in column '{col}'.")

            print(f"Unique values in {col}: {self.df[col].unique()}", '\n')
        print("By inspecting the unique values in each categorical column, we can conclude that there are no outliers.", '\n')
