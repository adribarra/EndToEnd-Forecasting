from __future__ import annotations

import pandas as pd


FEATURE_COLUMNS = [
    "store",
    "item",
    "promo",
    "day_of_week",
    "month",
    "week_of_year",
    "is_weekend",
    "lag_1",
    "lag_7",
    "rolling_mean_7",
]


def build_features(df: pd.DataFrame, target_col: str = "sales") -> pd.DataFrame:
    out = df.copy()
    out["date"] = pd.to_datetime(out["date"])
    out["day_of_week"] = out["date"].dt.dayofweek
    out["month"] = out["date"].dt.month
    out["week_of_year"] = out["date"].dt.isocalendar().week.astype(int)
    out["is_weekend"] = (out["day_of_week"] >= 5).astype(int)

    grouped = out.groupby(["store", "item"], group_keys=False)
    out["lag_1"] = grouped[target_col].shift(1)
    out["lag_7"] = grouped[target_col].shift(7)
    out["rolling_mean_7"] = grouped[target_col].transform(lambda s: s.shift(1).rolling(7).mean())
    return out


def prepare_training_matrix(df: pd.DataFrame, target_col: str = "sales") -> tuple[pd.DataFrame, pd.Series]:
    feats = build_features(df, target_col=target_col)
    clean = feats.dropna(subset=FEATURE_COLUMNS + [target_col]).copy()
    return clean[FEATURE_COLUMNS], clean[target_col]
