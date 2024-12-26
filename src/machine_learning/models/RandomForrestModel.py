from src.machine_learning.ModelTraining import ModelTraining
from sklearn.ensemble import RandomForestRegressor


class RandomForestModel(ModelTraining):
    """
    This class is responsible for training a Random Forest regression model.
    It inherits from the ModelTraining class, which provides methods for data preprocessing,
    training, and saving results.

    """

    def __init__(self):
        super().__init__()  # Initialize the parent ModelTraining class

    def train_random_forest(self):
        """
        Trains the Random Forest regression model using the dataset.
        The model is trained on the encoded dataset, and the training results are written to a file.
        """
        # Initialize the Random Forest Regressor model
        random_forest = RandomForestRegressor(random_state=42, n_estimators=100)

        # Perform one-hot encoding on the dataset to prepare it for training
        encoded_df = self._one_hot_encoding()

        # Train the model and save the results to a file
        self._train_and_write_to_file(random_forest, encoded_df, 'Random Forest')
