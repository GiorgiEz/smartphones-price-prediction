import pandas as pd

class SmartphonesDataset:
    _instance = None  # Class-level attribute to hold the single instance

    def __new__(cls, *args, **kwargs):
        """
        Overrides the default behavior of instance creation to ensure only one instance is created.
        """
        if cls._instance is None:
            cls._instance = super(SmartphonesDataset, cls).__new__(cls)
        return cls._instance

    def __init__(self, dataset_path='../../datasets/smartphones.csv'):
        """
        Initializes the SmartphonesDataset class by loading the dataset and defining key attributes.
        Ensures initialization happens only once.
        """
        if not hasattr(self, "initialized"):  # Avoid reinitialization
            if dataset_path is not None:
                try:
                    # Load the dataset
                    self.df = pd.read_csv(dataset_path)

                    # Define the target variable
                    self.target_variable = 'price'

                    # Define the numerical attributes
                    self.numerical_attributes = [
                        'price', 'avg_rating', '5G_or_not', 'num_cores', 'processor_speed', 'battery_capacity',
                        'fast_charging', 'ram_capacity', 'internal_memory', 'screen_size', 'refresh_rate',
                        'num_rear_cameras', 'primary_camera_rear', 'primary_camera_front',
                        'extended_memory_available', 'resolution_height', 'resolution_width'
                    ]

                    # Define the categorical attributes
                    self.categorical_attributes = ['brand_name', 'processor_brand', 'os']

                    print("SmartphonesDataset initialized successfully.")
                except FileNotFoundError:
                    print(f"Error: File not found at path: {dataset_path}")
                except Exception as e:
                    print(f"An error occurred during initialization: {e}")
            else:
                raise ValueError("Dataset path must be provided for the first initialization.")

            self.initialized = True  # Mark as initialized

    def get_dataframe(self):
        """Returns the loaded dataframe."""
        return self.df

    def get_target_variable(self):
        """Returns the target variable."""
        return self.target_variable

    def get_numerical_attributes(self):
        """Returns the list of numerical attributes."""
        return self.numerical_attributes

    def get_categorical_attributes(self):
        """Returns the list of categorical attributes."""
        return self.categorical_attributes
