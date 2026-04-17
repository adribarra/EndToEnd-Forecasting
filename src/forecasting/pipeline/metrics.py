from __future__ import annotations

import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error


def mae(y_true, y_pred) -> float:
    return float(mean_absolute_error(y_true, y_pred))


def rmse(y_true, y_pred) -> float:
    return float(np.sqrt(mean_squared_error(y_true, y_pred)))


def mape(y_true, y_pred) -> float:
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    denominator = np.where(y_true == 0, 1, y_true)
    return float(np.mean(np.abs((y_true - y_pred) / denominator)) * 100)
