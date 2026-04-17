from __future__ import annotations

from forecasting.models.classical import ProphetLikeModel, XGBoostLikeModel
from forecasting.models.deep import LSTMLikeModel


def get_model_registry() -> dict:
    return {
        "xgboost": XGBoostLikeModel(),
        "prophet": ProphetLikeModel(),
        "lstm": LSTMLikeModel(),
    }
