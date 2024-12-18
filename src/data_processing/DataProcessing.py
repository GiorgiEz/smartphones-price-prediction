class DataProcessing:
    def __init__(self, df):
        self.df = df

    def get_shape(self):
        print("SHAPE OF THE DATASET: ", self.df.shape, '\n')

    def get_info(self):
        print("DATASET INFORMATION: ")
        print(self.df.info(), '\n')

    def get_description(self):
        print("DESCRIPTION OF THE DATASET:\n")
        print(self.df.describe(), '\n')

    def get_null_columns(self):
        print("AMOUNT OF NULL VALUES IN EACH COLUMN:")
        print(self.df.isnull().sum(), '\n')

    def drop_fast_charging_available_col(self):
        try:
            # Check if the column exists before dropping
            if 'fast_charging_available' in self.df.columns:
                self.df.drop(columns=['fast_charging_available'], inplace=True)
                print("COLUMN 'fast_charging_available' DROPPED")
            else:
                print("COLUMN 'fast_charging_available' DOES NOT EXIST")

        except Exception as e:
            print(f"Error occurred while dropping the column: {e}")

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
        This ensures that the average rating for products with missing ratings is filled with
        a representative value, based on the overall datasets.
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
        """"""

    @fill_nulls('battery_capacity', lambda df: df['battery_capacity'].fillna(df['battery_capacity'].median()))
    def fill_battery_capacity_nulls(self):
        """"""

    @fill_nulls('fast_charging', lambda df: df['fast_charging'].fillna(0))
    def fill_fast_charging_nulls(self):
        """"""

    @fill_nulls('os', lambda df: df['os'].fillna('Unknown'))
    def fill_os_nulls(self):
        """"""

    @fill_nulls('primary_camera_front', lambda df: df['primary_camera_front'].fillna(df['primary_camera_front'].mode()[0]))
    def fill_primary_camera_front_nulls(self):
        """"""

    def save_cleaned_data(self):
        path = '../datasets/cleaned_smartphones.csv'
        self.df.to_csv(path, index=False)

    def main(self):
        self.get_shape()
        self.get_info()
        self.get_description()
        self.get_null_columns()
        self.drop_fast_charging_available_col()
        self.fill_avg_rating_nulls()
        self.fill_processor_brand_nulls()
        self.fill_num_cores_nulls()
        self.fill_processor_speed_nulls()
        self.fill_battery_capacity_nulls()
        self.fill_fast_charging_nulls()
        self.fill_os_nulls()
        self.fill_primary_camera_front_nulls()

        self.save_cleaned_data()
