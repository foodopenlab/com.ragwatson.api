from typing import Any

from titanic.app.walter_reader import WalterReader
from titanic.app.rose_model import RoseModel


class JackService:

    def __init__(self) -> None:
        self.walter = WalterReader()
        self.rose = RoseModel()

    def get_model_name_and_accuracy(self):
        return self.rose.get_model_name()
