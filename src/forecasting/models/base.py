from __future__ import annotations

from abc import ABC, abstractmethod


class ForecastModel(ABC):
    name: str

    @abstractmethod
    def fit(self, X, y) -> None:
        raise NotImplementedError

    @abstractmethod
    def predict(self, X):
        raise NotImplementedError
