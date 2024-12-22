from src.main.SmartphonesDataset import SmartphonesDataset
from src.exploratory_data_analysis.ExploratoryDataAnalysis import ExploratoryDataAnalysis
import matplotlib.pyplot as plt
import seaborn as sns


class PriceAnalysis(ExploratoryDataAnalysis):
    def __init__(self):
        super().__init__()
        self.smartphones_instance = SmartphonesDataset()
        self.df = self.smartphones_instance.get_dataframe()
        self.numerical_attributes = self.smartphones_instance.get_numerical_attributes()

    def correlation_bar_plots(self):
        """
        Plots two bar plots side by side:
        1. One for positive correlations with price.
        2. One for negative correlations with price.

        This function helps in distinguishing features with positive and negative
        correlations with the price column, showing how each one influences the price.
        """
        # Compute the correlation matrix for numerical features
        correlation_matrix = self.df[self.numerical_attributes].corr()
        price_correlation = correlation_matrix['price']

        # Separate positive and negative correlations
        positive_corr = price_correlation[price_correlation > 0].drop('price')
        negative_corr = price_correlation[price_correlation < 0]

        # Create the subplots (2 plots side by side)
        fig, axes = plt.subplots(1, 2, figsize=(14, 6))

        # Plot positive correlations
        sns.barplot(x=positive_corr.index, y=positive_corr.values, palette='Reds',
                    ax=axes[0], hue=positive_corr.index, legend=False)
        axes[0].set_title("Positive Correlations with Price", fontsize=14)
        axes[0].set_xlabel("Features", fontsize=12)
        axes[0].set_ylabel("Correlation Coefficient", fontsize=12)
        axes[0].tick_params(axis='x', rotation=45)

        # Plot negative correlations
        sns.barplot(x=negative_corr.index, y=negative_corr.values, palette='Blues',
                    ax=axes[1], hue=negative_corr.index, legend=False)
        axes[1].set_title("Negative Correlations with Price", fontsize=14)
        axes[1].set_xlabel("Features", fontsize=12)
        axes[1].set_ylabel("Correlation Coefficient", fontsize=12)
        axes[1].tick_params(axis='x', rotation=45)

        # Adjust layout for better readability
        plt.tight_layout()
        plt.show()

        """ 
        Observations:
        Most columns have positive correlation with price (internal_memory, 5g_or_not, avg_rating...).
        Only 3 columns have negative correlation with price (battery_capacity, num_cores, extended_memory_available).
        """

    def price_distribution_plot(self):
        """
        Plots a histogram with a Kernel Density Estimate (KDE) overlay
        to visualize the distribution of prices. This helps in understanding
        the skewness, spread, and potential outliers in the price column.
        """
        self.feature_distribution_plot('price')
