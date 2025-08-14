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
        random_forest = RandomForestRegressor(random_state=42, n_estimators=110)
        encoded_df, one_hot_maps = self._one_hot_encoding()

        return self._train_and_write_to_file(random_forest, encoded_df, 'Random Forest', one_hot_maps)
