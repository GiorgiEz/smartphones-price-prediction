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
        self.dataset = SmartphonesDataset()

    def fill_nulls(self, column_name, fill_value_func):
        """
        Fills missing values in the specified column using a provided fill function.

        Parameters:
        ----------
        column_name : The name of the column to fill missing values for.
        fill_value_func : A function that specifies how to fill the missing values for the column.
        """
        try:
            if column_name in self.dataset.get_df().columns:
                df = self.dataset.get_df()
                df[column_name] = fill_value_func(df)
                print(f"Null values in '{column_name}' column have been filled. "
                      f"Null values left: {df[column_name].isnull().sum()}")
            else:
                print(f"Column '{column_name}' does not exist.")
        except Exception as e:
            print(f"Error occurred while filling null values in '{column_name}': {e}")

    def fill_avg_rating_nulls(self):
        """
        Fills the missing values in the 'avg_rating' column with the mean of the non-null values.
        """
        self.fill_nulls('avg_rating',
                        lambda df: df['avg_rating'].fillna(round(df['avg_rating'].mean(), 1)))

    def fill_processor_brand_nulls(self):
        """
        Fills the missing values in the 'processor_brand' column with the value 'Unknown'.
        This is used to handle missing processor brand information in a way that marks
        those entries as unspecified, without losing the integrity of the data.
        """
        self.fill_nulls('processor_brand',
                        lambda df: df['processor_brand'].fillna('Unknown'))

    def fill_num_cores_nulls(self):
        """
        Fills the missing values in the 'num_cores' column with the most frequent value
        (mode) of the non-null entries. This helps maintain consistency in the data, as
        the number of cores should correspond to a common and discrete set of values.
        """
        self.fill_nulls('num_cores',
                        lambda df: df['num_cores'].fillna(df['num_cores'].mode()[0]))

    def fill_processor_speed_nulls(self):
        """
        Fills missing (NaN) values in the 'processor_speed' column using the median value of the column.
        The median is used to avoid skewness caused by outliers, ensuring the central tendency
        of the data is maintained for this numerical column.
        """
        self.fill_nulls('processor_speed',
                        lambda df: df['processor_speed'].fillna(df['processor_speed'].median()))

    def fill_battery_capacity_nulls(self):
        """
        Fills missing (NaN) values in the 'battery_capacity' column using the median value of the column.
        The median is selected as it provides a robust measure of central tendency, less affected by extreme values
        in this numerical column representing battery capacity.
        """
        self.fill_nulls('battery_capacity',
                        lambda df: df['battery_capacity'].fillna(df['battery_capacity'].median()))

    def fill_fast_charging_nulls(self):
        """
        Fills missing (NaN) values in the 'fast_charging' column with 0.
        Since 'fast_charging' is given in watts, filling it with 0 represents no fast charging.
        """
        self.fill_nulls('fast_charging',
                        lambda df: df['fast_charging'].fillna(0))

    def fill_os_nulls(self):
        """
        Fills missing (NaN) values in the 'os' column with 'other'.
        Since 'os' is a categorical column, missing values are assumed to represent unspecified or other
        operating systems, and they are replaced with the string 'other'.
        """
        self.fill_nulls('os',
                        lambda df: df['os'].fillna('other'))

    def fill_primary_camera_front_nulls(self):
        """
        Fills missing (NaN) values in the 'primary_camera_front' column using the most frequent value (mode).
        The mode is used because it is the most commonly occurring value, making it a logical choice
        for imputing missing values in this numerical column related to the front camera's resolution.
        """
        self.fill_nulls('primary_camera_front',
                        lambda df: df['primary_camera_front'].fillna(df['primary_camera_front'].mode()[0]))
