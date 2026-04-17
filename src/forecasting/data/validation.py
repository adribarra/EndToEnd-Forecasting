from __future__ import annotations

import pandas as pd


REQUIRED_COLUMNS = {"date", "store", "item", "sales"}


def validate_sales_data(df: pd.DataFrame) -> None:
    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")
    if df.empty:
        raise ValueError("Dataset is empty.")
    if df["sales"].isna().any():
        raise ValueError("Found null values in sales column.")
    if (df["sales"] < 0).any():
        raise ValueError("Found negative sales values.")
