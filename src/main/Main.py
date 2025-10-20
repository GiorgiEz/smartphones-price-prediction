from src.data_processing.RunDataProcessing import RunDataProcessing
from src.machine_learning.RunML import RunML
from src.price_prediction.predict import predict
from src.exploratory_data_analysis.RunEDA import RunEDA


if __name__ == '__main__':
    """ Part 1: Data Processing """
    data_processing = RunDataProcessing()  # Call data processing class
    data_processing.run_process()  # Perform data processing on the datasets

    """ Part 2: Exploratory Data Analysis """
    exploratory_data_analysis = RunEDA()  # Call exploratory data analysis class
    exploratory_data_analysis.run_visualizations()  # Run the visualizations of the dataset

    """ Part 3: Machine Learning """
    machine_learning = RunML()  # Call Machine Learning class
    machine_learning.run_prediction_models()  # Run ML prediction models

    """ Part 4: Price Prediction Using Example Input"""
    predict()
