from src.machine_learning.ModelTraining import ModelTraining
from sklearn.ensemble import GradientBoostingRegressor


class GradientBoostingModel(ModelTraining):
    """
    Class to train and evaluate a Gradient Boosting Regression model.
    Inherits from ModelTraining to reuse encoding and result saving methods.
    """

    def __init__(self):
        super().__init__()

    def train_gradient_boosting(self):
        """ Trains the Gradient Boosting Regression model and saves the results."""

        gradient_boosting = GradientBoostingRegressor(random_state=42, n_estimators=200, learning_rate=0.1)
        encoded_df, freq_maps = self._frequency_encoding()
        self._train_and_write_to_file(gradient_boosting, encoded_df, 'Gradient Boosting', freq_maps)
