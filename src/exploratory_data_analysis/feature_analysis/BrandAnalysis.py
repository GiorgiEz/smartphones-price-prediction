from src.exploratory_data_analysis.ExploratoryDataAnalysis import ExploratoryDataAnalysis
import matplotlib.pyplot as plt
import seaborn as sns


class BrandAnalysis(ExploratoryDataAnalysis):
    """
        A class for analyzing the brand feature of smartphones.

        Inherits from ExploratoryDataAnalysis class.

        Methods:
        -------
        avg_rating_by_brand()
        avg_price_by_brand()
        brand_distribution()
        pie_chart_5g_by_brand()
        pie_chart_fast_charging_by_brand()
        avg_rear_cameras_by_brand()
    """

    def __init__(self):
        super().__init__()

    def avg_rating_by_brand(self):
        """ Calls avg_feature_by_brand() with 'avg_rating' as the feature argument. """
        self.avg_feature_by_brand('avg_rating')

    def avg_price_by_brand(self):
        """ Calls avg_feature_by_brand() with 'price' as the feature argument. """
        self.avg_feature_by_brand('price')

    def brand_distribution(self):
        """
        Plots the distribution of smartphones across different brands and
        displays the count on top of each bar.

        This bar plot visualizes the count of smartphones for each brand,
        helping to understand which brands have the most or least devices.
        """
        brand_counts = self.df['brand_name'].value_counts() # Count the number of smartphones per brand

        # Plot the distribution
        plt.figure(figsize=(12, 6))
        sns.barplot(x=brand_counts.index, y=brand_counts.values, palette='viridis',
                    hue=brand_counts.index, legend=False)
        plt.title('Brand Distribution: Number of Smartphones per Brand', fontsize=14)
        plt.xlabel('Brand', fontsize=12)
        plt.ylabel('Number of Smartphones', fontsize=12)
        plt.xticks(rotation=90)  # Rotates brand names for better readability

        # Add numbers on top of each bar
        for index, value in enumerate(brand_counts.values):
            plt.text(index, value + 1, str(value), ha='center', va='bottom', fontsize=10)

        plt.tight_layout()
        plt.show()

    def pie_chart_5g_by_brand(self):
        """
        Plots a pie chart showing the percentage of 5G smartphones by brand.
        """
        self.pie_chart_feature_by_brand('5G_or_not')

    def pie_chart_fast_charging_by_brand(self):
        """
        Plots a pie chart showing the percentage of 5G smartphones by brand.
        """
        self.pie_chart_feature_by_brand('fast_charging')

    def avg_rear_cameras_by_brand(self):
        """ Plots a bar chart showing the average number of rear cameras by brand. """
        camera_counts = self.df.groupby('brand_name')['num_rear_cameras'].mean().sort_values(ascending=False).head(10)
        plt.figure(figsize=(10, 6))
        sns.barplot(x=camera_counts.index, y=camera_counts.values,
                    palette='Blues', hue=camera_counts.index, legend=False)
        plt.title('Average Number of Rear Cameras by Brand', fontsize=14)
        plt.xlabel('Brand', fontsize=12)
        plt.ylabel('Average Number of Cameras', fontsize=12)
        plt.xticks(rotation=45)
        plt.show()

