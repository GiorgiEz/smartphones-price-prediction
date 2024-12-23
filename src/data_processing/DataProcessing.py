from src.main.SmartphonesDataset import SmartphonesDataset
import requests


class DataProcessing:
    """
        A class for data processing on a dataset.

        Attributes:
        ----------
        df : pandas.DataFrame
            The dataset to be processed.

        Methods:
        -------
        get_shape()
        get_info()
        get_description()
        get_null_columns()
        drop_fast_charging_available_col()
        convert_inr_to_usd()
        save_cleaned_data()
        run_process()
    """

    def __init__(self):
        self.df = SmartphonesDataset().get_dataframe()
        self.categorical_attributes = SmartphonesDataset().get_categorical_attributes()

    def get_shape(self):
        """
        Prints the shape of the dataset (number of rows and columns).
        Useful for quickly understanding the size of the dataset.
        """
        print("SHAPE OF THE DATASET: ", self.df.shape, '\n')

    def get_info(self):
        """
        Prints detailed information about the dataset, including column names, data types,
        and non-null counts for each column. Helpful for understanding the dataset structure.
        """
        print("DATASET INFORMATION: ")
        print(self.df.info(), '\n')

    def get_description(self):
        """
        Prints a statistical summary of the dataset for numerical columns. Includes metrics like mean,
        min, max, standard deviation, etc. Useful for a quick overview of data distribution.
        """
        print("DESCRIPTION OF THE DATASET:\n")
        print(self.df.describe(), '\n')

    def get_null_columns(self):
        """
        Prints the count of missing (null) values for each column in the dataset.
        Useful for identifying columns with missing data that may need imputation.
        """
        print("AMOUNT OF NULL VALUES IN EACH COLUMN:")
        print(self.df.isnull().sum(), '\n')

    def drop_fast_charging_available_col(self):
        """
        Since fast_charging_available is a binary column and fast_charging column only contains values
        if fast_charging_available is True, we can drop this column, and add default value in
        fast_charging column, corresponding to fast_charging_available is False.
        """
        try:
            # Check if the column exists before dropping
            if 'fast_charging_available' in self.df.columns:
                self.df.drop(columns=['fast_charging_available'], inplace=True)
                print("COLUMN 'fast_charging_available' DROPPED")
            else:
                print("COLUMN 'fast_charging_available' DOES NOT EXIST")

        except Exception as e:
            print(f"Error occurred while dropping the column: {e}")

    def convert_inr_to_usd(self, to_currency='USD'):
        """
        Since prices are provided in INR we can use real-time currency API to convert prices from INR to USD.

        Parameters:
        - to_currency (str): The currency to convert prices to. Defaults to 'USD'

        This method fetches the latest INR to USD conversion rate and applies it to the specified column.
        """
        try:
            price_col = 'price'
            # Fetch the latest exchange rate (replace with your API of choice)
            response = requests.get("https://api.exchangerate-api.com/v4/latest/INR")
            response.raise_for_status()  # Raise an exception for HTTP errors
            exchange_data = response.json()
            inr_to_new_currency_rate = exchange_data['rates'][to_currency.upper()]
            # print(f"Current INR to {to_currency} rate: {inr_to_new_currency_rate}")

            # Ensure the INR column exists
            if price_col in self.df.columns:
                self.df[price_col] = round(self.df[price_col] * inr_to_new_currency_rate)
                print(f"Converted price to '{to_currency}' from INR.")
            else:
                print("Column price does not exist in the dataset.")
        except requests.exceptions.RequestException as e:
            print(f"Error fetching exchange rate: {e}")
        except Exception as e:
            print(f"Error occurred while converting INR to {to_currency}: {e}")
        print()

    def deduplication(self):
        """
        Removes duplicate rows from the dataset based on the 'model' column.
        Ensures only unique entries for each model remain in the dataset.
        """
        try:
            if 'model' in self.df.columns:
                before_count = len(self.df)
                self.df = self.df.drop_duplicates(subset=['model'])
                after_count = len(self.df)
                print(f"Removed {before_count - after_count} duplicate entries based on 'model'.")
            else:
                print("COLUMN 'model' DOES NOT EXIST IN THE DATASET.")
        except Exception as e:
            print(f"Error occurred while removing duplicates: {e}")

    def save_cleaned_data(self):
        """ Saves the dataset in separate csv file after processing is done."""

        path = '../../datasets/cleaned_smartphones.csv'
        self.df.to_csv(path, index=False)
