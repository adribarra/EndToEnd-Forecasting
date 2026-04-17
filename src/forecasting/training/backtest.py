from __future__ import annotations

import json

from forecasting.data.loader import load_sales_data
from forecasting.features.pipeline import FEATURE_COLUMNS, prepare_training_matrix
from forecasting.models.registry import get_model_registry
from forecasting.pipeline.backtesting import walk_forward_backtest


def main() -> None:
    df = load_sales_data()
    if len(df) > 80_000:
        df = df.sort_values("date").tail(80_000).reset_index(drop=True)
    X, y = prepare_training_matrix(df)
    work_df = X.copy()
    work_df["sales"] = y
    rows = []
    for model in get_model_registry().values():
        rows.append(walk_forward_backtest(work_df, model, FEATURE_COLUMNS, "sales").__dict__)
    print(json.dumps(rows, indent=2))


if __name__ == "__main__":
    main()
