from sklearn.linear_model import LinearRegression
from src.machine_learning.ModelTraining import ModelTraining


class LinearModel(ModelTraining):
    """
    Class to train and evaluate a Linear Regression model.
    Inherits from ModelTraining to reuse encoding and result saving methods.
    """

    def __init__(self):
        super().__init__()

    def train_linear_regression(self):
        """ Trains the Linear Regression model and saves the results. """

        linear_regression = LinearRegression()  # Initialize the Linear Regression model
        encoded_df, one_hot_maps = self._one_hot_encoding()  # Encode categorical features
        self._train_and_write_to_file(linear_regression, encoded_df, 'Linear Regression', one_hot_maps)
