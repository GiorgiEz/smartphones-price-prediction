from src.main.SmartphonesDataset import SmartphonesDataset
import matplotlib.pyplot as plt
import seaborn as sns


class ExploratoryDataAnalysis:
    def __init__(self):
        self.smartphones_instance = SmartphonesDataset()
        self.df = self.smartphones_instance.get_dataframe()
        self.numerical_attributes = self.smartphones_instance.get_numerical_attributes()

    def correlation_heatmap(self):
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

    def feature_distribution_plot(self, column_name):
        price_data = self.df[column_name]

        # Plot the histogram with KDE overlay
        plt.figure(figsize=(10, 6))
        sns.histplot(price_data, kde=True, color='skyblue', bins=30,
                     stat='density', linewidth=0)

        # Set the title and labels
        plt.title(f'{column_name} Distribution with KDE Overlay', fontsize=14)
        plt.xlabel(column_name, fontsize=12)
        plt.ylabel('Density', fontsize=12)

        plt.show()

    def avg_feature_by_brand(self, col_name):
        """
        Plots two bar plots on the same image: one for the top 10 brands with the highest average "col_name"
        and one for the least 10 brands with the lowest average "col_name", displaying values on top of each bar.
        """
        # Sort the dataframe by the average feature for each brand
        brand_ratings = self.df.groupby('brand_name')[col_name].mean().sort_values()

        # Select the top 10 and least 10 brands based on the feature
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
