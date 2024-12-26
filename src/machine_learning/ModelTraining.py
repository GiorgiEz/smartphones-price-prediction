from src.main.SmartphonesDataset import SmartphonesDataset
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import pandas as pd


class ModelTraining:
    """
    This class is responsible for training machine learning models on a smartphone dataset.
    It handles feature engineering, model training, and performance evaluation.
    The results are saved to a text file for later analysis.

    Attributes:
        _dataset (SmartphonesDataset): Dataset instance used for loading and managing data.
        _df (pd.DataFrame): The raw dataframe containing the smartphone dataset.
        _cat_attributes (list): List of categorical features in the dataset.
        _target_var (str): The target variable for model training.
        _results_file_path (str): File path ('model_results.txt') to store model evaluation results.

    Methods:
        __init__(self): Initializes the class and loads the dataset.
        _get_feature_df(df): Prepares feature dataframe for model training.
        _add_derived_features(df): Adds derived features for machine learning.
        _one_hot_encoding(): Applies one-hot encoding to categorical features.
        _frequency_encoding(): Applies frequency encoding to categorical features.
        _train_model(model, encoded_df): Trains the model and returns evaluation metrics.
        _train_and_write_to_file(model, encoded_df, model_name): Trains the model and writes results to a file.
    """

    def __init__(self):
        self._dataset = SmartphonesDataset()
        self._df = self._dataset.get_df()
        self._cat_attributes = self._dataset.get_categorical_attributes()
        self._target_var = self._dataset.get_target_var()
        self._results_file_path = 'model_results.txt'

    def _get_feature_df(self, df):
        """
        Drops model and price columns from df and returns it.
        It's used for defining the features dataframe before train_test_split.
        """
        df = df.copy()
        if 'model' in df.columns:
            df = df.drop(columns=['model'])
        if self._target_var in df.columns:
            df = df.drop(columns=[self._target_var])
        return df

    def _add_derived_features(self, df):
        """
        Adds derived features to the dataframe for ML analysis.

        Parameters: df (pd.DataFrame): The input dataframe with required columns.
        Returns: pd.DataFrame: The dataframe with new derived columns added.
        """
        df = df.copy()

        df['processor_power'] = df['num_cores'] * df['processor_speed']
        df['price_per_core'] = df['price'] / df['num_cores']
        df['price_per_gb_ram'] = df['price'] / df['ram_capacity']
        df['battery_life_indicator'] = df['battery_capacity'] / df['processor_speed']
        df['pixel_density'] = (df['resolution_height'] * df['resolution_width']) / (df['screen_size'] ** 2)
        df['camera_pixel_quality'] = df['primary_camera_rear'] + df['primary_camera_front']
        df['performance_index'] = (
                0.3 * df['num_cores'] + 0.3 * df['ram_capacity'] +
                0.3 * df['processor_speed'] + 0.1 * df['internal_memory']
        )
        return df

    def _one_hot_encoding(self):
        """ Implements one-hot encoding for categorical features. """
        return pd.get_dummies(self._df, columns=self._cat_attributes, dtype='int')

    def _frequency_encoding(self):
        """ Implements frequency encoding for categorical features. """
        encoded_df = self._df.copy()
        for category in self._cat_attributes:
            freq_encoding = encoded_df[category].value_counts() / len(encoded_df)
            encoded_df[category] = encoded_df[category].map(freq_encoding)
        return encoded_df

    def _train_model(self, model, encoded_df):
        """ Trains the given model and returns the scores from testing the model. """

        X = self._get_feature_df(encoded_df)
        y = encoded_df[self._target_var]

        # Split the dataset into training and testing sets (80% training, 20% testing)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        return (mean_squared_error(y_test, y_pred),
                mean_absolute_error(y_test, y_pred), r2_score(y_test, y_pred))

    def _train_and_write_to_file(self, model, encoded_df, model_name):
        """ Trains the given model and writes the results to file. """
        # We perform feature engineering on encoded dataframe
        derived_features_df = self._add_derived_features(encoded_df)

        # Before feature engineering
        mse_before, mae_before, r2_before = self._train_model(model, encoded_df)

        # After feature engineering
        mse_after, mae_after, r2_after = self._train_model(model, derived_features_df)

        # A comparison table
        results = pd.DataFrame({
            "Metric": ["MSE", "MAE", "R2"],
            "Before Feature Engineering": [mse_before, mae_before, r2_before],
            "After Feature Engineering": [mse_after, mae_after, r2_after],
        })

        # Save the results in a TXT file
        try:
            with open(self._results_file_path, 'a') as f:
                f.write(f"\nTraining {model_name}: \n")
                f.write(results.to_string() + '\n')
            print(f"Results written successfully! for {model_name} \n")
        except Exception as e:
            print(f"Error: {e}")
