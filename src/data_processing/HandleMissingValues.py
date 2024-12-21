from src.main.SmartphonesDataset import SmartphonesDataset


class HandleMissingValues:
    """
        A class for handling missing values in a dataset.

        Attributes:
        ----------
        df : pandas.DataFrame
            The dataset to be processed.

        Methods:
        -------
        fill_nulls()
        fill_avg_rating_nulls()
        fill_processor_brand_nulls()
        fill_num_cores_nulls()
        fill_processor_speed_nulls()
        fill_battery_capacity_nulls()
        fill_fast_charging_nulls()
        fill_os_nulls()
        fill_primary_camera_front_nulls()
    """

    def __init__(self):
        self.df = SmartphonesDataset().get_dataframe()

    @staticmethod
    def fill_nulls(column_name, fill_value_func):
        """
        A decorator function that fills missing (NaN) values in a specified column of a DataFrame.
        It checks if the column exists, applies the given fill value function to fill missing values,
        and prints the updated null count for the column.

        Parameters:
        column_name (str): The name of the column to fill missing values for.
        fill_value_func (function): A function that specifies how to fill the missing values for the column.

        Returns:
        decorator (function): A decorator function that wraps the target method.
        """

        def decorator(func):
            def wrapper(self):
                try:
                    # Check if the column exists
                    if column_name in self.df.columns:
                        # Apply the fill value function to fill NaN values
                        self.df[column_name] = fill_value_func(self.df)
                        # Print the updated status
                        print(f"Null values in '{column_name}' column have been filled. "
                              f"Null values left: {self.df[column_name].isnull().sum()}")
                    else:
                        print(f"COLUMN '{column_name}' DOES NOT EXIST")
                except Exception as e:
                    print(f"Error occurred while filling null values in '{column_name}': {e}")

            return wrapper

        return decorator

    @fill_nulls('avg_rating', lambda df: df['avg_rating'].fillna(round(df['avg_rating'].mean(), 1)))
    def fill_avg_rating_nulls(self):
        """
        Fills the missing values in the 'avg_rating' column with the mean of the non-null values.
        """

    @fill_nulls('processor_brand', lambda df: df['processor_brand'].fillna('Unknown'))
    def fill_processor_brand_nulls(self):
        """
        Fills the missing values in the 'processor_brand' column with the value 'Unknown'.
        This is used to handle missing processor brand information in a way that marks
        those entries as unspecified, without losing the integrity of the data.
        """

    @fill_nulls('num_cores', lambda df: df['num_cores'].fillna(df['num_cores'].mode()[0]))
    def fill_num_cores_nulls(self):
        """
        Fills the missing values in the 'num_cores' column with the most frequent value
        (mode) of the non-null entries. This helps maintain consistency in the data, as
        the number of cores should correspond to a common and discrete set of values.
        """

    @fill_nulls('processor_speed', lambda df: df['processor_speed'].fillna(df['processor_speed'].median()))
    def fill_processor_speed_nulls(self):
        """
        Fills missing (NaN) values in the 'processor_speed' column using the median value of the column.
        The median is used to avoid skewness caused by outliers, ensuring the central tendency
        of the data is maintained for this numerical column.
        """

    @fill_nulls('battery_capacity', lambda df: df['battery_capacity'].fillna(df['battery_capacity'].median()))
    def fill_battery_capacity_nulls(self):
        """
        Fills missing (NaN) values in the 'battery_capacity' column using the median value of the column.
        The median is selected as it provides a robust measure of central tendency, less affected by extreme values
        in this numerical column representing battery capacity.
        """

    @fill_nulls('fast_charging', lambda df: df['fast_charging'].fillna(0))
    def fill_fast_charging_nulls(self):
        """
        Fills missing (NaN) values in the 'fast_charging' column with 0.
        Since 'fast_charging' is given in watts, filling it with 0 represents no fast charging.
        """

    @fill_nulls('os', lambda df: df['os'].fillna('Unknown'))
    def fill_os_nulls(self):
        """
        Fills missing (NaN) values in the 'os' column with 'Unknown'.
        Since 'os' is a categorical column, missing values are assumed to represent unspecified or unknown
        operating systems, and they are replaced with the string 'Unknown'.
        """

    @fill_nulls('primary_camera_front',
                lambda df: df['primary_camera_front'].fillna(df['primary_camera_front'].mode()[0]))
    def fill_primary_camera_front_nulls(self):
        """
        Fills missing (NaN) values in the 'primary_camera_front' column using the most frequent value (mode).
        The mode is used because it is the most commonly occurring value, making it a logical choice
        for imputing missing values in this numerical column related to the front camera's resolution.
        """
