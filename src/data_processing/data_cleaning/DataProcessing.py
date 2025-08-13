from src.data_processing.SmartphonesDataset import SmartphonesDataset
import requests


class DataProcessing:
    """
        A class for data processing on a dataset.

        Attributes:
        ----------
        df : The dataset to be processed.

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
        self.dataset = SmartphonesDataset()

    def get_shape(self):
        """
        Prints the shape of the dataset (number of rows and columns).
        Useful for quickly understanding the size of the dataset.
        """
        print("SHAPE OF THE DATASET: ", self.dataset.get_df().shape, '\n')

    def get_info(self):
        """
        Prints detailed information about the dataset, including column names, data types,
        and non-null counts for each column. Helpful for understanding the dataset structure.
        """
        print("DATASET INFORMATION: ")
        print(self.dataset.get_df().info(), '\n')

    def get_description(self):
        """
        Prints a statistical summary of the dataset for numerical columns. Includes metrics like mean,
        min, max, standard deviation, etc. Useful for a quick overview of data distribution.
        """
        print("DESCRIPTION OF THE DATASET:\n")
        print(self.dataset.get_df().describe(), '\n')

    def get_null_columns(self):
        """
        Prints the count of missing (null) values for each column in the dataset.
        Useful for identifying columns with missing data that may need imputation.
        """
        print("AMOUNT OF NULL VALUES IN EACH COLUMN:")
        print(self.dataset.get_df().isnull().sum(), '\n')

    def drop_fast_charging_available_col(self):
        """
        Since fast_charging_available is a binary column and fast_charging column only contains values
        if fast_charging_available is True, we can drop this column, and add default value in
        fast_charging column, corresponding to fast_charging_available is False.
        """
        try:
            # Check if the column exists before dropping
            if 'fast_charging_available' in self.dataset.get_df().columns:
                self.dataset.get_df().drop(columns=['fast_charging_available'], inplace=True)
                print("COLUMN 'fast_charging_available' DROPPED")
            else:
                print("COLUMN 'fast_charging_available' DOES NOT EXIST")

        except Exception as e:
            print(f"Error occurred while dropping the column: {e}")

    def convert_inr_to_usd(self, to_currency='USD'):
        """
        Converts prices in INR to the specified currency using the real-time exchange rate.
        If the API request fails, a constant exchange rate is used as a fallback.

        Parameters:
        - to_currency (str): The currency to convert prices to. Defaults to 'USD'.

        This method fetches the latest INR to USD conversion rate and applies it to the price column.
        If the API fails, a fallback conversion rate is used.
        """
        price_col = 'price'
        try:
            # Attempt to fetch the latest exchange rate from the API
            response = requests.get("https://api.exchangerate-api.com/v4/latest/INR")
            response.raise_for_status()  # Raise an exception for HTTP errors
            exchange_data = response.json()
            inr_to_new_currency_rate = exchange_data['rates'][to_currency.upper()]
            print(f"Fetched INR to {to_currency} conversion rate from API: {inr_to_new_currency_rate}")
        except requests.exceptions.RequestException as e:
            print(f"Error fetching exchange rate from API: {e}")
            # Fallback to a constant exchange rate if the API call fails
            inr_to_new_currency_rate = 0.012  # Example fallback rate (INR to USD)
            print(f"Using fallback conversion rate: INR to {to_currency} = {inr_to_new_currency_rate}")
        except Exception as e:
            print(f"Error occurred while converting INR to {to_currency}: {e}")
            # Fallback rate in case of any other errors
            inr_to_new_currency_rate = 0.012
            print(f"Using fallback conversion rate: INR to {to_currency} = {inr_to_new_currency_rate}")

        # Ensure the price column exists in the dataset
        if price_col in self.dataset.get_df().columns:
            self.dataset.get_df()[price_col] = (
                round(self.dataset.get_df()[price_col] * inr_to_new_currency_rate, 2))
            print(f"Converted price to '{to_currency}' from INR.")
        else:
            print("Column 'price' does not exist in the dataset.")
        print()

    def deduplication(self):
        """
        Removes duplicate rows from the dataset based on the 'model' column.
        Ensures only unique entries for each model remain in the dataset.
        """
        df = self.dataset.get_df()
        try:
            if 'model' in df.columns:
                before_count = len(df)
                df.drop_duplicates(subset=['model'], inplace=True)
                after_count = len(df)
                print(f"Removed {before_count - after_count} duplicate entries based on 'model'.\n")
            else:
                print("COLUMN 'model' DOES NOT EXIST IN THE DATASET.")
        except Exception as e:
            print(f"Error occurred while removing duplicates: {e}")

    def save_cleaned_data(self):
        """ Saves the dataset in separate csv file after processing is done."""

        path = '../../datasets/cleaned_smartphones.csv'
        self.dataset.get_df().to_csv(path, index=False)
