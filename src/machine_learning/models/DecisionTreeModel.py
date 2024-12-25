from src.machine_learning.TrainModels import TrainModels
from sklearn.tree import DecisionTreeRegressor


class DecisionTreeModel(TrainModels):
    def __init__(self):
        super().__init__()

    def train_decision_tree(self):
        df_one_hot_encoded = self._one_hot_encoding()
        decision_tree = DecisionTreeRegressor(random_state=42)
        print("Training Decision Tree")
        self._train_model(decision_tree, df_one_hot_encoded)
