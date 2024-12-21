from src.data_processing.HandleOutliers import HandleOutliers
from src.data_processing.HandleMissingValues import HandleMissingValues
from src.main.SmartphonesDataset import SmartphonesDataset
import requests
from sklearn.preprocessing import LabelEncoder


class DataProcessing:
    """
        A class for handling missing values in a dataset.

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

    def encode_categorical_attributes(self):
        """ Uses label encoding to encode categorical attributes and replace them with numerical values."""
        la = LabelEncoder()
        for col in self.categorical_attributes:
            self.df[col] = la.fit_transform(self.df[col])

    def save_cleaned_data(self):
        """ Saves the dataset in separate csv file after processing is done."""

        path = '../../datasets/cleaned_smartphones.csv'
        self.df.to_csv(path, index=False)

    def run_process(self):
        """ Runs the data processing pipeline. This method is called by the main script."""

        # General description of the dataset
        self.get_shape()
        self.get_info()
        self.get_description()
        self.get_null_columns()

        self.drop_fast_charging_available_col() # dropping fast_charging_available column
        self.convert_inr_to_usd() # converting price

        # Handling outliers
        handle_outliers = HandleOutliers()
        handle_outliers.check_num_features_for_outliers()
        handle_outliers.check_categorical_features_for_outliers()

        # Handling null values
        handle_missing_values = HandleMissingValues()
        handle_missing_values.fill_avg_rating_nulls()
        handle_missing_values.fill_processor_brand_nulls()
        handle_missing_values.fill_num_cores_nulls()
        handle_missing_values.fill_processor_speed_nulls()
        handle_missing_values.fill_battery_capacity_nulls()
        handle_missing_values.fill_fast_charging_nulls()
        handle_missing_values.fill_os_nulls()
        handle_missing_values.fill_primary_camera_front_nulls()

        self.encode_categorical_attributes() # Encoding of categorical attributes to numerical values
        self.save_cleaned_data() # Saving the cleaned data in its own csv file
