from __future__ import annotations

import math
from datetime import timedelta

import numpy as np
import pandas as pd


def simulate_sales_data(
    start_date: str = "2021-01-01",
    periods: int = 365,
    n_stores: int = 3,
    n_items: int = 10,
    seed: int = 42,
) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    dates = pd.date_range(start=start_date, periods=periods, freq="D")
    rows = []
    for store in range(1, n_stores + 1):
        for item in range(1, n_items + 1):
            base = rng.integers(20, 80)
            trend = rng.uniform(0.01, 0.08)
            for i, date in enumerate(dates):
                seasonality = 10 * math.sin((2 * math.pi * i) / 7) + 4 * math.sin((2 * math.pi * i) / 30)
                promo = int(rng.random() < 0.12)
                noise = rng.normal(0, 3)
                sales = max(0, base + trend * i + seasonality + (12 * promo) + noise)
                rows.append(
                    {
                        "date": date,
                        "store": store,
                        "item": item,
                        "promo": promo,
                        "sales": float(round(sales, 2)),
                    }
                )
    return pd.DataFrame(rows)


def create_future_frame(df: pd.DataFrame, horizon: int = 8) -> pd.DataFrame:
    latest = pd.to_datetime(df["date"]).max()
    keys = df[["store", "item"]].drop_duplicates()
    rows = []
    for _, key in keys.iterrows():
        for step in range(1, horizon + 1):
            rows.append(
                {
                    "date": latest + timedelta(days=step),
                    "store": int(key["store"]),
                    "item": int(key["item"]),
                    "promo": 0,
                }
            )
    return pd.DataFrame(rows)
