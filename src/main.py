import pandas as pd
from data_processing.DataProcessing import DataProcessing


if __name__ == '__main__':
    smartphones_data_path = '../datasets/smartphones.csv'  # path to smartphones csv file
    df = pd.read_csv(smartphones_data_path) # load smartphones data using pandas library

    data_processing = DataProcessing(df) # Call data processing class
    data_processing.main() # Perform data processing on the datasets
