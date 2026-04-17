from __future__ import annotations

import argparse
import json
from datetime import datetime

import joblib

from forecasting.config.settings import METRICS_DIR, MODELS_DIR
from forecasting.data.loader import load_sales_data
from forecasting.features.pipeline import FEATURE_COLUMNS, prepare_training_matrix
from forecasting.models.registry import get_model_registry
from forecasting.pipeline.backtesting import walk_forward_backtest


def run_training() -> dict:
    MODELS_DIR.mkdir(parents=True, exist_ok=True)
    METRICS_DIR.mkdir(parents=True, exist_ok=True)

    df = load_sales_data()
    if len(df) > 80_000:
        df = df.sort_values("date").tail(80_000).reset_index(drop=True)
    X, y = prepare_training_matrix(df)
    training_df = X.copy()
    training_df["sales"] = y

    registry = get_model_registry()
    results = []
    for _, model in registry.items():
        result = walk_forward_backtest(training_df, model, FEATURE_COLUMNS, "sales")
        results.append(result)

    best = min(results, key=lambda r: r.rmse)
    best_model = registry[best.model]
    best_model.fit(X, y)

    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    model_path = MODELS_DIR / f"{best.model}_{timestamp}.joblib"
    joblib.dump(best_model, model_path)

    payload = {
        "timestamp": timestamp,
        "champion_model": best.model,
        "model_path": str(model_path),
        "metrics": [r.__dict__ for r in results],
    }
    with open(METRICS_DIR / f"training_report_{timestamp}.json", "w", encoding="utf-8") as fh:
        json.dump(payload, fh, indent=2)
    with open(MODELS_DIR / "latest_model.json", "w", encoding="utf-8") as fh:
        json.dump({"model_path": str(model_path), "model_name": best.model, "timestamp": timestamp}, fh, indent=2)
    return payload


def main() -> None:
    parser = argparse.ArgumentParser(description="Run batch training and model selection.")
    parser.parse_args()
    report = run_training()
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
