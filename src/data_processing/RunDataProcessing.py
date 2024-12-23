from src.data_processing.data_cleaning.HandleOutliers import HandleOutliers
from src.data_processing.data_cleaning.HandleMissingValues import HandleMissingValues
from src.data_processing.data_cleaning.DataProcessing import DataProcessing


class RunDataProcessing:
    """
        Main class for running the data processing pipeline.

        Attributes:
        ----------
        data_processing : instance of DataProcessing class
        handle_outliers : instance of HandleOutliers class
        handle_missing_values : instance of HandleMissingValues class

        Methods:
        -------
        run_process()
    """

    def __init__(self):
        self.data_processing = DataProcessing()
        self.handle_outliers = HandleOutliers()
        self.handle_missing_values = HandleMissingValues()

    def run_process(self):
        """ Runs the data processing pipeline. This method is called by the main script."""

        # General description of the dataset
        self.data_processing.get_shape()
        self.data_processing.get_info()
        self.data_processing.get_description()
        self.data_processing.get_null_columns()

        self.data_processing.drop_fast_charging_available_col()  # dropping fast_charging_available column
        self.data_processing.convert_inr_to_usd()  # converting price
        self.data_processing.deduplication()  # remove the duplicates

        # Handling outliers
        self.handle_outliers.check_num_features_for_outliers()
        self.handle_outliers.check_categorical_features_for_outliers()

        # Handling null values
        self.handle_missing_values.fill_avg_rating_nulls()
        self.handle_missing_values.fill_processor_brand_nulls()
        self.handle_missing_values.fill_num_cores_nulls()
        self.handle_missing_values.fill_processor_speed_nulls()
        self.handle_missing_values.fill_battery_capacity_nulls()
        self.handle_missing_values.fill_fast_charging_nulls()
        self.handle_missing_values.fill_os_nulls()
        self.handle_missing_values.fill_primary_camera_front_nulls()

        self.data_processing.save_cleaned_data()  # Saving the cleaned data in its own csv file
