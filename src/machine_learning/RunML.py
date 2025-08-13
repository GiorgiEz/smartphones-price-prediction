from src.machine_learning.models.GradientBoostingModel import GradientBoostingModel
from src.machine_learning.models.RandomForrestModel import RandomForestModel


class RunML:
    """
    This class is responsible for running multiple machine learning models.
    It initializes the models and trains them by calling their respective training functions.

    Attributes:
    self._results_file_path (str): File path ('model_results.txt') to store model evaluation results.
    linear_model (LinearModel): An instance of the LinearModel class for linear regression.
    random_forest_model (RandomForestModel): An instance of the RandomForestModel class for random forest regression.
    gradient_boosting_model (GradientBoostingModel): An instance of the GradientBoostingModel class for gradient
    boosting regression.
    decision_tree_model (DecisionTreeModel): An instance of the DecisionTreeModel class for
    decision tree regression.
    """

    def __init__(self):
        """
        Initializes the RunML class with instances of different machine learning models.
        """
        self._results_file_path = 'model_results.txt'
        self.random_forest_model = RandomForestModel()  # Random forest model
        self.gradient_boosting_model = GradientBoostingModel()  # Gradient boosting model

    def run_prediction_models(self):
        """
        Runs all the initialized machine learning models by calling their respective training functions.
        """
        results = {"Random Forest": self.random_forest_model.train_random_forest(),
                   "Gradient Boosting": self.gradient_boosting_model.train_gradient_boosting()}

        # Write results in file
        try:
            with open(self._results_file_path, 'w') as f:
                for model_name, result in results.items():
                    f.write(f"\nTraining {model_name}: \n")
                    f.write(result.to_string() + '\n')
                    print(f"Results written successfully! for {model_name} \n")
        except Exception as e:
            print(f"Error: {e}")
