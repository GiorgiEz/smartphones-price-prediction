from src.machine_learning.models.DecisionTreeModel import DecisionTreeModel
from src.machine_learning.models.GradientBoostingModel import GradientBoostingModel
from src.machine_learning.models.LinearModel import LinearModel
from src.machine_learning.models.RandomForrestModel import RandomForestModel


class RunML:
    """
    This class is responsible for running multiple machine learning models.
    It initializes the models and trains them by calling their respective training functions.

    Attributes:
        linear_model (LinearModel): An instance of the LinearModel class for linear regression.
        random_forest_model (RandomForestModel): An instance of the RandomForestModel class for random forest regression.
        gradient_boosting_model (GradientBoostingModel): An instance of the GradientBoostingModel class for gradient boosting regression.
        decision_tree_model (DecisionTreeModel): An instance of the DecisionTreeModel class for decision tree regression.
    """

    def __init__(self):
        """
        Initializes the RunML class with instances of different machine learning models.
        """
        self.linear_model = LinearModel()  # Linear regression model
        self.random_forest_model = RandomForestModel()  # Random forest model
        self.gradient_boosting_model = GradientBoostingModel()  # Gradient boosting model
        self.decision_tree_model = DecisionTreeModel()  # Decision tree model

    def run_prediction_models(self):
        """
        Runs all the initialized machine learning models by calling their respective training functions.
        """
        # Train the linear regression model
        self.linear_model.train_linear_regression()

        # Train the random forest regression model
        self.random_forest_model.train_random_forest()

        # Train the gradient boosting regression model
        self.gradient_boosting_model.train_gradient_boosting()

        # Train the decision tree regression model
        self.decision_tree_model.train_decision_tree()
