from pathlib import Path

import joblib
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

_APP = Path(__file__).resolve().parent
ROSE_DECISION_TREE_JOBLIB = _APP / "rose_decision_tree.joblib"
_CSV = _APP / "Titanic-Dataset.csv"


def _ensure_decision_tree_joblib() -> None:
    if ROSE_DECISION_TREE_JOBLIB.exists():
        return
    df = pd.read_csv(_CSV)
    cols = ["Pclass", "Age", "SibSp", "Parch", "Fare", "Survived"]
    data = df[cols].dropna()
    X = data.drop(columns=["Survived"])
    y = data["Survived"]
    model = DecisionTreeClassifier(max_depth=5, random_state=42)
    model.fit(X, y)
    joblib.dump(model, ROSE_DECISION_TREE_JOBLIB)


class RoseModel:
    def __init__(self) -> None:
        _ensure_decision_tree_joblib()
        self.model = joblib.load(ROSE_DECISION_TREE_JOBLIB)

    def get_model_name(self) -> str:
        return type(self.model).__name__
