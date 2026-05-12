from fastapi import FastAPI

from .jack_service import JackService
from .rose_model import ROSE_DECISION_TREE_JOBLIB

app = FastAPI(title="Titanic (JamesController)")


class JamesController:
    def __init__(self):
        self.service = JackService()

    def get_data(self):
        return self.service.walter.get_data()

    def get_count(self):
        return self.service.walter.get_count()

    def has_decision_tree_model(self) -> bool:
        return ROSE_DECISION_TREE_JOBLIB.exists()

    def get_model_name_and_accuracy(self):
        return self.service.get_model_name_and_accuracy()
