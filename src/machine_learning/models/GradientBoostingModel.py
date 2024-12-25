from src.machine_learning.TrainModels import TrainModels
from sklearn.ensemble import GradientBoostingRegressor


class GradientBoostingModel(TrainModels):
    def __init__(self):
        super().__init__()

    def train_gradient_boosting(self):
        df_label_encoded = self._one_hot_encoding()
        gradient_boosting = GradientBoostingRegressor(random_state=42, n_estimators=100, learning_rate=0.1)
        print("Training Gradient Boosting Regressor")
        self._train_model(gradient_boosting, df_label_encoded)
