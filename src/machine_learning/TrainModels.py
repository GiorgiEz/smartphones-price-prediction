from sklearn.preprocessing import LabelEncoder
from src.main.SmartphonesDataset import SmartphonesDataset
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import pandas as pd


class TrainModels:
    def __init__(self):
        self._dataset = SmartphonesDataset()
        self._df = self._dataset.get_df()
        self._cat_attributes = self._dataset.get_categorical_attributes()
        self._target_var = self._dataset.get_target_var()

    def drop_unnecessary_columns(self, encoded_df):
        encoded_df = encoded_df.copy()
        if 'model' in encoded_df.columns:
            encoded_df = encoded_df.drop(columns=['model'])
        if self._target_var in encoded_df.columns:
            encoded_df = encoded_df.drop(columns=[self._target_var])
        return encoded_df

    def _one_hot_encoding(self):
        return pd.get_dummies(self._df, columns=self._cat_attributes, dtype='int')

    def _label_encoding(self):
        le = LabelEncoder()
        encoded_df = self._df.copy()
        for category in self._cat_attributes:
            encoded_df[category] = le.fit_transform(encoded_df[category])
        return encoded_df

    def _frequency_encoding(self):
        encoded_df = self._df.copy()
        for category in self._cat_attributes:
            freq_encoding = encoded_df[category].value_counts() / len(encoded_df)
            encoded_df[category] = encoded_df[category].map(freq_encoding)
        return encoded_df

    def _train_model(self, model, encoded_df):
        X = self.drop_unnecessary_columns(encoded_df)
        y = encoded_df[self._target_var]

        # Split the dataset into training and testing sets (80% training, 20% testing)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        # Evaluate the model
        mse = mean_squared_error(y_test, y_pred)
        mae = mean_absolute_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)

        # Print evaluation metrics
        print(f"Mean Squared Error (MSE): {mse:.2f}")
        print(f"Mean Absolute Error (MAE): {mae:.2f}")
        print(f"R-squared (R2): {r2:.2f}\n")
