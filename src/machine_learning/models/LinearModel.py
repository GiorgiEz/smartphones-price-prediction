from sklearn.linear_model import LinearRegression
from src.machine_learning.TrainModels import TrainModels


class LinearModel(TrainModels):
    def __init__(self):
        super().__init__()

    def train_linear_regression(self):
        df_one_hot_encoded = self._one_hot_encoding()
        linear_regression = LinearRegression()
        print("Training Linear Regression")
        self._train_model(linear_regression, df_one_hot_encoded)
