from __future__ import annotations

from dataclasses import dataclass

import pandas as pd

from forecasting.pipeline.metrics import mae, mape, rmse


@dataclass
class BacktestResult:
    model: str
    mae: float
    rmse: float
    mape: float


def walk_forward_backtest(df: pd.DataFrame, model, feature_cols: list[str], target_col: str) -> BacktestResult:
    split_idx = int(len(df) * 0.8)
    train = df.iloc[:split_idx]
    test = df.iloc[split_idx:]
    model.fit(train[feature_cols], train[target_col])
    pred = model.predict(test[feature_cols])
    return BacktestResult(
        model=model.name,
        mae=mae(test[target_col], pred),
        rmse=rmse(test[target_col], pred),
        mape=mape(test[target_col], pred),
    )
