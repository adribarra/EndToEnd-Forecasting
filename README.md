# End To End Forecasting (In Progress)

End-to-end demand forecasting system with:
- Batch training
- Backtesting and comparative metrics (MAE, RMSE, MAPE)
- FastAPI prediction service
- Model versioning by artifact metadata
- Dashboard for model comparison
- Docker and CI

## Project Structure

- [`src/`](src/) - application source package and modules ([details](src/README.md))
- [`dashboards/`](dashboards/) - visualization apps and reporting UI ([details](dashboards/README.md))
- [`tests/`](tests/) - automated unit and smoke tests ([details](tests/README.md))

## Quickstart

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -e ".[dev,dashboard]"
```

## Train + Backtest

```bash
forecast-train
forecast-backtest
```

This creates artifacts under `artifacts/models` and `artifacts/metrics`.

## Run API

```bash
uvicorn forecasting.api.app:app --reload
```

Endpoints:
- `GET /health`
- `GET /model/info`
- `POST /forecast`

Example request payload:

```json
{
  "store": 1,
  "item": 3,
  "promo": 0,
  "lag_1": 120.5,
  "lag_7": 110.2,
  "rolling_mean_7": 115.1,
  "day_of_week": 2,
  "month": 4,
  "week_of_year": 16,
  "is_weekend": 0
}
```

## Dashboard

```bash
streamlit run dashboards/streamlit_app.py
```

## Tests and Lint

```bash
ruff check src tests
pytest -q
```

## Docker

```bash
docker build -t forecasting-api .
docker run -p 8000:8000 forecasting-api
```

## Dataset

If `dataset/retail_sales.csv` is not available, training automatically uses a synthetic simulator.
