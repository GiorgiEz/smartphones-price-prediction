from src.exploratory_data_analysis.ExploratoryDataAnalysis import ExploratoryDataAnalysis
import matplotlib.pyplot as plt
import seaborn as sns
import textwrap


class ModelAnalysis(ExploratoryDataAnalysis):
    """
        A class for analyzing the model feature of smartphones.

        Inherits from ExploratoryDataAnalysis class.

        Methods:
        -------
        most_expensive_and_highest_rated_models()
        pie_chart_5g_and_memory_distribution()
        price_comparison_by_5g()
    """

    def __init__(self):
        super().__init__()

    def most_expensive_and_highest_rated_models(self):
        """
        Plots two bar plots side by side:
        1. Most expensive smartphone models.
        2. Highest-rated smartphone models.
        """
        # Most expensive models
        most_expensive = self.df.sort_values(by='price', ascending=False).head(10)
        most_expensive['model'] = most_expensive['model'].apply(
            lambda x: '\n'.join(textwrap.wrap(x, width=15))  # Wrap long names
        )

        # Highest-rated models
        highest_rated = self.df.sort_values(by='avg_rating', ascending=False).head(10)
        highest_rated['model'] = highest_rated['model'].apply(
            lambda x: '\n'.join(textwrap.wrap(x, width=15))  # Wrap long names
        )

        fig, axes = plt.subplots(1, 2, figsize=(18, 6)) # Create a figure with two subplots

        # Bar plot for most expensive models
        sns.barplot(
            x='model', y='price', data=most_expensive, palette='viridis', ax=axes[0],
            hue='model', dodge=False, legend=False
        )
        axes[0].set_title('Most Expensive Smartphones', fontsize=14)
        axes[0].set_xlabel('Model', fontsize=12)
        axes[0].set_ylabel('Price', fontsize=12)
        axes[0].tick_params(axis='x', rotation=30, labelsize=8)

        # Add values on top of bars for most expensive models
        for container in axes[0].containers:
            axes[0].bar_label(container, fmt='%.0f', fontsize=8, label_type='edge')

        # Bar plot for highest-rated models
        sns.barplot(
            x='model', y='avg_rating', data=highest_rated, palette='coolwarm', ax=axes[1],
            hue='model', dodge=False, legend=False
        )
        axes[1].set_title('Highest Rated Smartphones', fontsize=14)
        axes[1].set_xlabel('Model', fontsize=12)
        axes[1].set_ylabel('Average Rating', fontsize=12)
        axes[1].tick_params(axis='x', rotation=30, labelsize=8)

        # Add values on top of bars for highest-rated models
        for container in axes[1].containers:
            axes[1].bar_label(container, fmt='%.2f', fontsize=8, label_type='edge')

        plt.tight_layout()
        plt.show()

    def pie_chart_5g_and_memory_distribution(self):
        """
        Plots two pie charts:
        1. The percentage of smartphone models with and without 5G.
        2. The percentage of smartphone models with and without extended memory.
        """
        # Count the number of smartphones with and without 5G
        five_g_count = self.df['5G_or_not'].value_counts()

        # Count the number of smartphones with and without extended memory
        extended_memory_count = self.df['extended_memory_available'].value_counts()

        # Create a figure with two subplots
        fig, axes = plt.subplots(1, 2, figsize=(16, 8))

        # Pie chart for 5G distribution
        axes[0].pie(
            five_g_count,
            labels=['With 5G', 'Without 5G'],
            autopct='%1.1f%%',  # Display percentage on the chart
            startangle=90,
            colors=['#66b3ff', '#ff9999'],
            explode=[0.1, 0],  # Slightly explode the first slice (with 5G)
            wedgeprops={'edgecolor': 'black'},
        )
        axes[0].set_title('Percentage of Models with and without 5G', fontsize=14)

        # Pie chart for extended memory availability distribution
        axes[1].pie(
            extended_memory_count,
            labels=['With Extended Memory', 'Without Extended Memory'],
            autopct='%1.1f%%',  # Display percentage on the chart
            startangle=90,
            colors=['#99ff99', '#ffcc99'],
            explode=[0.1, 0],  # Slightly explode the first slice (with extended memory)
            wedgeprops={'edgecolor': 'black'},
        )
        axes[1].set_title('Percentage of Models with and without Extended Memory', fontsize=14)

        # Display the plot
        plt.tight_layout()
        plt.show()

    def price_comparison_by_5g(self):
        """ Plots a boxplot to compare the price of 5G and non-5G smartphones. """

        sns.boxplot(x='5G_or_not', y='price', data=self.df, palette='Set1', hue='5G_or_not', legend=False)
        plt.title('Price Comparison Between 5G and Non-5G Smartphones', fontsize=14)
        plt.xlabel('5G Support', fontsize=12)
        plt.ylabel('Price', fontsize=12)
        plt.xticks([0, 1], ['Without 5G', 'With 5G'])

        # Calculate the average price for 5G and non-5G smartphones
        avg_price_5g = round(self.df[self.df['5G_or_not'] == 1]['price'].mean())
        avg_price_non_5g = round(self.df[self.df['5G_or_not'] == 0]['price'].mean())

        # Display the average prices on the plot
        plt.text(0, avg_price_non_5g - 500, f'${avg_price_non_5g:.2f}', horizontalalignment='center', fontsize=12,
                 color='black')
        plt.text(1, avg_price_5g - 800, f'${avg_price_5g:.2f}', horizontalalignment='center', fontsize=12, color='black')

        # Show the plot
        plt.show()
