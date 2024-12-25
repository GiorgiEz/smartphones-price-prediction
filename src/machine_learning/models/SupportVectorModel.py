from src.machine_learning.TrainModels import TrainModels
from sklearn.svm import SVR
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split


class SupportVectorModel(TrainModels):
    def __init__(self):
        super().__init__()

    def train_and_tune(self, svr, encoded_df):
        X = self.drop_unnecessary_columns(encoded_df)
        y = encoded_df[self._target_var]

        # Split the dataset into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Define the grid of hyperparameters to search
        param_grid = {
            'C': [1000, 100000],  # Regularization parameter
            'epsilon': [1, 100],  # Tolerance margin
            'kernel': ['rbf', 'poly']  # Kernel types
        }

        # Perform GridSearchCV
        grid_search = GridSearchCV(estimator=svr, param_grid=param_grid,
                                   scoring='r2', cv=10, n_jobs=-1, verbose=1)
        grid_search.fit(X_train, y_train)

        print(f"Best parameters: {grid_search.best_params_}")  # Best parameters and score
        best_model = grid_search.best_estimator_  # Evaluate on test set
        self._train_model(best_model, encoded_df)

    def train_svr(self):
        encoded_df = self._label_encoding()
        svr = SVR()
        print("Training Support Vector Regressor (SVR): \n")
        self._train_model(svr, encoded_df)  # Default model
        self.train_and_tune(svr, encoded_df)  # With tuning

        """ 
        Observations: 
        On default SVR performs horribly with -0.12 R-squared score, after tuning, the best chosen
        parameters are {'C': 100000, 'epsilon': 100, 'kernel': 'rbf'} and the R-squared score
        increases to 0.74. Encoding didn't really matter as the difference was minimal.
        """
