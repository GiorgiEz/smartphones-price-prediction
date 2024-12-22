from src.exploratory_data_analysis.ExploratoryDataAnalysis import ExploratoryDataAnalysis
from src.exploratory_data_analysis.feature_analysis.PriceAnalysis import PriceAnalysis
from src.exploratory_data_analysis.feature_analysis.RatingAnalysis import RatingAnalysis
from src.exploratory_data_analysis.feature_analysis.BrandAnalysis import BrandAnalysis


class RunEDA:
    def __init__(self):
        self.price_analysis = PriceAnalysis()
        self.rating_analysis = RatingAnalysis()
        self.brand_analysis = BrandAnalysis()
        self.exploratory_data_analysis = ExploratoryDataAnalysis()

    def run_visualizations(self):
        """ Runs all the visualizations for exploratory data analysis"""

        self.exploratory_data_analysis.correlation_heatmap()

        # Analyzing price
        self.price_analysis.correlation_bar_plots()
        self.price_analysis.price_distribution_plot()

        # Analyzing avg_rating
        self.rating_analysis.avg_rating_distribution_plot()
        self.rating_analysis.avg_rating_vs_price()

        # Analyzing brands
        self.brand_analysis.avg_rating_by_brand()
        self.brand_analysis.avg_price_by_brand()
        self.brand_analysis.brand_distribution()
        self.brand_analysis.pie_chart_5g_by_brand()
