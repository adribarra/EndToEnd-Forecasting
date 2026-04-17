from __future__ import annotations

from pathlib import Path

import pandas as pd
from pandas.api.types import is_string_dtype

from forecasting.config.settings import DATA_DIR
from forecasting.data.simulation import simulate_sales_data
from forecasting.data.validation import validate_sales_data


def _normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    if "store" not in out.columns and "store_id" in out.columns:
        out["store"] = out["store_id"]
    if "item" not in out.columns and "item_id" in out.columns:
        out["item"] = out["item_id"]
    if is_string_dtype(out["store"]):
        out["store"] = out["store"].astype(str).str.extract(r"(\d+)").astype(int)
    if is_string_dtype(out["item"]):
        out["item"] = out["item"].astype(str).str.extract(r"(\d+)").astype(int)
    return out


def load_sales_data(path: Path | None = None) -> pd.DataFrame:
    data_path = path or DATA_DIR / "retail_sales.csv"
    if Path(data_path).exists():
        df = pd.read_csv(data_path)
    else:
        df = simulate_sales_data()
    df = _normalize_columns(df)
    df["date"] = pd.to_datetime(df["date"])
    validate_sales_data(df)
    return df.sort_values(["store", "item", "date"]).reset_index(drop=True)
