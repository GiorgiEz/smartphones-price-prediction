from src.data_processing.SmartphonesDataset import SmartphonesDataset
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import pandas as pd
import joblib


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

    def _one_hot_encoding(self):
        """ Implements one-hot encoding for categorical features and returns mapping. """
        encoded_df = pd.get_dummies(self._df, columns=self._cat_attributes, dtype='int')

        # Create a mapping: original column name -> list of new one-hot columns
        one_hot_maps = {}
        for col in self._cat_attributes:
            one_hot_maps[col] = [c for c in encoded_df.columns if c.startswith(col + "_")]

        return encoded_df, one_hot_maps

    def _frequency_encoding(self):
        """ Implements frequency encoding for categorical features and returns mapping. """
        encoded_df = self._df.copy()
        freq_maps = {}
        for category in self._cat_attributes:
            freq_encoding = encoded_df[category].value_counts() / len(encoded_df)
            freq_maps[category] = freq_encoding.to_dict()
            encoded_df[category] = encoded_df[category].map(freq_maps[category])
        return encoded_df, freq_maps

    def _train_model(self, model, encoded_df):
        """ Trains the given model and returns the scores from testing the model. """

        X = self._get_feature_df(encoded_df)
        y = encoded_df[self._target_var]

        # Split the dataset into training and testing sets (80% training, 20% testing)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        return (mean_squared_error(y_test, y_pred),
                mean_absolute_error(y_test, y_pred),
                r2_score(y_test, y_pred),
                model)

    def _train_and_write_to_file(self, model, encoded_df, model_name, encoding_maps):
        """ Trains the given model and writes the results to file. """
        mse_before, mae_before, r2_before, trained_model = self._train_model(model, encoded_df)

        feature_columns = self._get_feature_df(encoded_df).columns.tolist()

        # Save trained model & feature order
        save_path = f"saved_models/{model_name.replace(' ', '_').lower()}_model.pkl"

        if model_name == 'Gradient Boosting':
            joblib.dump({
                "model": trained_model,
                "features": feature_columns,
                "maps": encoding_maps,
                "type": "frequency"
            }, save_path)
        else:
            joblib.dump({
                "model": trained_model,
                "features": feature_columns,
                "maps": encoding_maps,
                "type": "one-hot"
            }, save_path)

        print(f"✅ Model saved to {save_path}")

        # A comparison table
        return pd.DataFrame({
            "Metric": ["MSE", "MAE", "R2"],
            "Scores": [mse_before, mae_before, r2_before]
        })
