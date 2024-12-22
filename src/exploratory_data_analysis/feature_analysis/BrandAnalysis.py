from src.exploratory_data_analysis.ExploratoryDataAnalysis import ExploratoryDataAnalysis
from src.main.SmartphonesDataset import SmartphonesDataset
import matplotlib.pyplot as plt
import seaborn as sns


class BrandAnalysis(ExploratoryDataAnalysis):
    def __init__(self):
        super().__init__()
        self.smartphones_instance = SmartphonesDataset()
        self.df = self.smartphones_instance.get_dataframe()
        self.numerical_attributes = self.smartphones_instance.get_numerical_attributes()

    def avg_rating_by_brand(self):
        """
        Plots two box plots on the same image: one for the top 10 brands with the highest average ratings
        and one for the least 10 brands with the lowest average ratings.
        """
        self.avg_feature_by_brand('avg_rating')

    def avg_price_by_brand(self):
        """
        Plots two box plots on the same image: one for the top 10 brands with the highest average prices
        and one for the least 10 brands with the lowest average prices.
        """
        self.avg_feature_by_brand('price')

    def brand_distribution(self):
        """
        Plots the distribution of smartphones across different brands and
        displays the count on top of each bar.

        This bar plot visualizes the count of smartphones for each brand,
        helping to understand which brands have the most or least devices.
        """
        # Count the number of smartphones per brand
        brand_counts = self.df['brand_name'].value_counts()

        # Plot the distribution
        plt.figure(figsize=(12, 6))
        sns.barplot(x=brand_counts.index, y=brand_counts.values, palette='viridis', hue=brand_counts.index, legend=False)
        plt.title('Brand Distribution: Number of Smartphones per Brand', fontsize=14)
        plt.xlabel('Brand', fontsize=12)
        plt.ylabel('Number of Smartphones', fontsize=12)
        plt.xticks(rotation=90)  # Rotate brand names for better readability

        # Add numbers on top of each bar
        for index, value in enumerate(brand_counts.values):
            plt.text(index, value + 1, str(value), ha='center', va='bottom', fontsize=10)

        plt.tight_layout()
        plt.show()

    def pie_chart_5g_by_brand(self):
        """
        Plots a pie chart showing the percentage of 5G smartphones by brand.
        """
        # Filter the dataframe to only include 5G smartphones
        df_5g = self.df[self.df['5G_or_not'] == 1]

        # Count the number of 5G smartphones for each brand (top 10)
        brand_5g_counts = df_5g['brand_name'].value_counts().head(10)

        # Plot the pie chart
        plt.figure(figsize=(10, 8))
        brand_5g_counts.plot.pie(
            autopct='%1.1f%%',
            startangle=90,
            cmap='tab20',
            legend=False,
            labels=brand_5g_counts.index,
            explode=[0.05, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01],
        )

        plt.title('Percentage of 5G Smartphones by Brand', fontsize=14)
        plt.ylabel('')
        plt.show()
