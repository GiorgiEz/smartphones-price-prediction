from src.machine_learning.TrainModels import TrainModels
from sklearn.ensemble import RandomForestRegressor


class RandomForestModel(TrainModels):
    def __init__(self):
        super().__init__()

    def train_random_forest(self):
        df_label_encoded = self._one_hot_encoding()
        random_forest = RandomForestRegressor(random_state=42, n_estimators=100)
        print("Training Random Forest Regressor")
        self._train_model(random_forest, df_label_encoded)

