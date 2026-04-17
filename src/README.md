# Source Code

This folder contains the Python package for the end-to-end forecasting system.

## Package layout

- `forecasting/config`: project settings and common paths.
- `forecasting/data`: data loading, simulation, and validation.
- `forecasting/features`: feature engineering pipeline.
- `forecasting/models`: model abstractions and model registry.
- `forecasting/pipeline`: backtesting and metrics.
- `forecasting/training`: batch training and comparison CLI workflows.
- `forecasting/api`: FastAPI service and request/response schemas.
- `forecasting/utils`: shared utilities (reserved for future use).

## Entry points

- `forecast-train`: trains models, performs model selection, saves artifacts.
- `forecast-backtest`: runs model comparison with MAE, RMSE, and MAPE.

## Conventions

- Keep modules focused and testable.
- Prefer reusable functions over notebook-only logic.
- Save runtime artifacts under `artifacts/`, not in `src/`.
