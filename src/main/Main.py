from src.data_processing.RunDataProcessing import RunDataProcessing
from src.exploratory_data_analysis.RunEDA import RunEDA

if __name__ == '__main__':
    """ Part 1 """
    data_processing = RunDataProcessing()  # Call data processing class
    data_processing.run_process()  # Perform data processing on the datasets

    """ Part 2 """
    exploratory_data_analysis = RunEDA()  # Call exploratory data analysis class
    exploratory_data_analysis.run_visualizations()  # Run the visualizations of the dataset
