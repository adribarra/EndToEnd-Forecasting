from __future__ import annotations

from dataclasses import dataclass

from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression

from forecasting.models.base import ForecastModel


@dataclass
class XGBoostLikeModel(ForecastModel):
    name: str = "xgboost"

    def __post_init__(self) -> None:
        try:
            from xgboost import XGBRegressor

            self.model = XGBRegressor(
                n_estimators=150,
                max_depth=6,
                learning_rate=0.08,
                objective="reg:squarederror",
                random_state=42,
            )
        except Exception:
            # Fallback keeps the pipeline runnable without optional deps.
            self.model = RandomForestRegressor(n_estimators=60, max_depth=12, random_state=42, n_jobs=-1)

    def fit(self, X, y) -> None:
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)


@dataclass
class ProphetLikeModel(ForecastModel):
    name: str = "prophet"

    def __post_init__(self) -> None:
        self.model = LinearRegression()

    def fit(self, X, y) -> None:
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)
