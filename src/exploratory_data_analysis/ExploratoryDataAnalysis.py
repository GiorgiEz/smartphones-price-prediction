from src.main.SmartphonesDataset import SmartphonesDataset
import matplotlib.pyplot as plt
import seaborn as sns


class ExploratoryDataAnalysis:
    """
        A class for exploratory data analysis (EDA) on smartphones dataset.

        Attributes:
        ----------
        smartphones_instance : Instance of SmartphonesDataset class
        df: pandas.DataFrame
        numerical_attributes: list of numerical attributes of smartphones dataset

        Methods:
        -------
        correlation_heatmap()
        processor_speed_strip_plot()
        os_pie_chart()
        feature_distribution_plot()
        avg_feature_by_brand()
        pie_chart_feature_by_brand()
    """

    def __init__(self):
        self.smartphones_instance = SmartphonesDataset()
        self.df = self.smartphones_instance.get_dataframe()
        self.numerical_attributes = self.smartphones_instance.get_numerical_attributes()

    def correlation_heatmap(self):
        """ Displays the correlation heatmap of numerical attributes. """
        correlation_matrix = self.df[self.numerical_attributes].corr()

        # Plot the heatmap
        plt.figure(figsize=(10, 8))
        sns.heatmap(correlation_matrix, annot=True, fmt='.2f', linewidths=0.5, annot_kws={"size": 10})

        # Adjust tick labels to show column names fully
        plt.xticks(rotation=60, ha='right', fontsize=10)
        plt.yticks(fontsize=9)

        # Adjust the position of the heatmap
        plt.subplots_adjust(left=0.2, bottom=0.2, right=0.95, top=0.95)

        plt.title('Correlation Heatmap')
        plt.show()

    def processor_speed_strip_plot(self):
        """ Displays a strip plot of processor speed by processor brand. """
        plt.figure(figsize=(10, 6))
        sns.stripplot(x='processor_brand', y='processor_speed', data=self.df,
                      palette='Set2', hue='processor_brand', jitter=True, legend=False)
        plt.title('Processor Speed by Processor Brand', fontsize=14)
        plt.xlabel('Processor Brand', fontsize=12)
        plt.ylabel('Processor Speed (GHz)', fontsize=12)
        plt.xticks(rotation=45, fontsize=8)
        plt.show()

    def os_pie_chart(self):
        """ Displays a pie chart of operating system distribution. """
        os_counts = self.df['os'].value_counts()

        plt.figure(figsize=(8, 8))
        os_counts.plot.pie(autopct='%1.1f%%', startangle=90, cmap='Set3', explode=[0.05] + [0] * len(os_counts[1:]))
        plt.title('Operating System Distribution', fontsize=14)
        plt.ylabel('')
        plt.show()

    def feature_distribution_plot(self, col_name):
        """ Displays a histogram with KDE overlay of a given feature."""

        plt.figure(figsize=(10, 6))
        sns.histplot(self.df[col_name], kde=True, color='skyblue', bins=30,
                     stat='density', linewidth=0)

        plt.title(f'{col_name} Distribution with KDE Overlay', fontsize=14)
        plt.xlabel(col_name, fontsize=12)
        plt.ylabel('Density', fontsize=12)

        plt.show()

    def avg_feature_by_brand(self, col_name):
        """
        Plots two bar plots on the same image: one for the top 10 brands with the highest average "col_name"
        and one for the least 10 brands with the lowest average "col_name", displaying values on top of each bar.
        """
        # Sort the dataframe by the average feature for each brand
        brand_ratings = self.df.groupby('brand_name')[col_name].mean().sort_values()

        top_10_brands = brand_ratings.tail(10)  # Top 10 highest averages
        least_10_brands = brand_ratings.head(10)  # Least 10 lowest averages

        # Filter the dataframe for only these brands
        top_brands_df = (self.df[self.df['brand_name'].isin(top_10_brands.index)]
                         .sort_values(by=col_name, ascending=False))

        least_brands_df = (self.df[self.df['brand_name'].isin(least_10_brands.index)]
                           .sort_values(by=col_name, ascending=False))

        # Create a figure with two subplots
        fig, axes = plt.subplots(1, 2, figsize=(18, 6))

        # Plot for the top 10 brands with the highest averages
        sns.barplot(x='brand_name', y=col_name, data=top_brands_df, palette='Blues',
                    ax=axes[0], hue='brand_name', legend=False)
        axes[0].set_title(f'Top 10 Brands with Highest Average {col_name}', fontsize=14)
        axes[0].set_xlabel('Brand', fontsize=12)
        axes[0].set_ylabel(f'Average {col_name}', fontsize=12)
        axes[0].tick_params(axis='x', rotation=0)

        # Add numbers on top of each bar for the top 10 brands
        for index, value in enumerate(
                top_brands_df.groupby('brand_name')[col_name].mean().sort_values(ascending=False)):
            axes[0].text(index, value + 0.02, f'{value:.2f}', ha='center', va='bottom', fontsize=10)

        # Plot for the least 10 brands with the lowest averages
        sns.barplot(x='brand_name', y=col_name, data=least_brands_df, palette='Reds',
                    ax=axes[1], hue='brand_name', legend=False)
        axes[1].set_title(f'Top 10 Brands with Lowest Average {col_name}', fontsize=14)
        axes[1].set_xlabel('Brand', fontsize=12)
        axes[1].set_ylabel(f'Average {col_name}', fontsize=12)
        axes[1].tick_params(axis='x', rotation=0)

        # Add numbers on top of each bar for the least 10 brands
        for index, value in enumerate(
                least_brands_df.groupby('brand_name')[col_name].mean().sort_values(ascending=False)):
            axes[1].text(index, value + 0.02, f'{value:.2f}', ha='center', va='bottom', fontsize=10)

        # Display the plot
        plt.tight_layout()
        plt.show()

    def pie_chart_feature_by_brand(self, col_name):
        """ Plots a pie chart showing the percentage of features by brand. """

        # Calculate percentage based on all 5G smartphones, not just the top 10
        brand_feature_counts = self.df[self.df[col_name] > 0]['brand_name'].value_counts()
        top_10_counts = brand_feature_counts.head(10) # Select top 10 brands

        # Plot the pie chart
        plt.figure(figsize=(10, 8))
        top_10_counts.plot.pie(
            autopct='%1.1f%%',
            startangle=90,
            cmap='tab20',
            legend=False,
            labels=top_10_counts.index,
            explode=[0.05] + [0.01] * 9,
        )

        plt.title(f'Percentage of {col_name} Smartphones by Top 10 Brands', fontsize=14)
        plt.ylabel('')
        plt.show()
