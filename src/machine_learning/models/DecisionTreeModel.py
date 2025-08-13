from src.machine_learning.ModelTraining import ModelTraining
from sklearn.tree import DecisionTreeRegressor


class DecisionTreeModel(ModelTraining):
    """
    Class to train and evaluate a Decision Tree Regression model.
    Inherits from ModelTraining to reuse encoding and result saving methods.
    """

    def __init__(self):
        super().__init__()

    def train_decision_tree(self):
        """ Trains the Decision Tree model and saves the results. """

        decision_tree = DecisionTreeRegressor(random_state=42)
        encoded_df, one_hot_maps = self._one_hot_encoding()
        self._train_and_write_to_file(decision_tree, encoded_df, 'Decision Tree', one_hot_maps)

