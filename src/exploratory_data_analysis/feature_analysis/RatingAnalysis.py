from src.exploratory_data_analysis.ExploratoryDataAnalysis import ExploratoryDataAnalysis
import matplotlib.pyplot as plt
import seaborn as sns


class RatingAnalysis(ExploratoryDataAnalysis):
    """
        A class for analyzing the avg_rating feature of smartphones.

        Inherits from ExploratoryDataAnalysis class.

        Methods:
        -------
        avg_rating_distribution_plot()
        avg_rating_vs_price()
    """

    def __init__(self):
        super().__init__()

    def avg_rating_distribution_plot(self):
        """
        Plots a histogram with a Kernel Density Estimate (KDE) overlay
        to visualize the distribution of avg_ratings. This helps in understanding
        the skewness, spread, and potential outliers in the avg_rating column.
        """
        self.feature_distribution_plot('avg_rating')

    def avg_rating_vs_price(self):
        """
        Plots a scatter plot to show the relationship between average rating and price.
        Helps to understand if higher-priced phones tend to have higher or lower ratings.
        """
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x='price', y='avg_rating', data=self.df, color='blue', alpha=0.6)
        plt.title('Average Rating vs Price', fontsize=14)
        plt.xlabel('Price', fontsize=12)
        plt.ylabel('Average Rating', fontsize=12)
        plt.show()
