from __future__ import annotations

from dataclasses import dataclass

from sklearn.neural_network import MLPRegressor

from forecasting.models.base import ForecastModel


@dataclass
class LSTMLikeModel(ForecastModel):
    name: str = "lstm"

    def __post_init__(self) -> None:
        # Lightweight fallback that does not require tensorflow in CI.
        self.model = MLPRegressor(hidden_layer_sizes=(32, 16), random_state=42, max_iter=150)

    def fit(self, X, y) -> None:
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)
