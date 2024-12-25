from src.machine_learning.models.SupportVectorModel import SupportVectorModel


class RunML:
    def __init__(self):
        self.support_vector_model = SupportVectorModel()

    def run_prediction_models(self):
        self.support_vector_model.train_svr()
