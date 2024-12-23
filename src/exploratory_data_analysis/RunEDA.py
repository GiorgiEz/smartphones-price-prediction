from src.exploratory_data_analysis.ExploratoryDataAnalysis import ExploratoryDataAnalysis
from src.exploratory_data_analysis.feature_analysis.PriceAnalysis import PriceAnalysis
from src.exploratory_data_analysis.feature_analysis.RatingAnalysis import RatingAnalysis
from src.exploratory_data_analysis.feature_analysis.BrandAnalysis import BrandAnalysis
from src.exploratory_data_analysis.feature_analysis.ModelAnalysis import ModelAnalysis


class RunEDA:
    """
        A class for running all the exploratory data analysis visualizations.

        Attributes:
        ----------
        exploratory_data_analysis : instance of ExploratoryDataAnalysis class
        price_analysis : instance of PriceAnalysis class
        rating_analysis : instance of RatingAnalysis class
        brand_analysis : instance of BrandAnalysis class
        model_analysis : instance of ModelAnalysis class

        Methods:
        -------
        run_visualizations()
    """

    def __init__(self):
        self.exploratory_data_analysis = ExploratoryDataAnalysis()
        self.price_analysis = PriceAnalysis()
        self.rating_analysis = RatingAnalysis()
        self.brand_analysis = BrandAnalysis()
        self.model_analysis = ModelAnalysis()

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
        self.brand_analysis.brand_distribution()
        self.brand_analysis.avg_rating_by_brand()
        self.brand_analysis.avg_price_by_brand()
        self.brand_analysis.pie_chart_5g_by_brand()
        self.brand_analysis.pie_chart_fast_charging_by_brand()
        self.brand_analysis.avg_rear_cameras_by_brand()

        # Analyzing models
        self.model_analysis.most_expensive_and_highest_rated_models()
        self.model_analysis.pie_chart_5g_and_memory_distribution()
        self.model_analysis.price_comparison_by_5g()

        # General analysis
        self.exploratory_data_analysis.processor_speed_strip_plot()
        self.exploratory_data_analysis.os_pie_chart()
