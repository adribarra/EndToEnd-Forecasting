from __future__ import annotations

import json

import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException

from forecasting.api.schemas import ForecastRequest, ForecastResponse
from forecasting.config.settings import MODELS_DIR
from forecasting.features.pipeline import FEATURE_COLUMNS

app = FastAPI(title="End-to-End Forecasting API", version="0.1.0")


def _load_latest_model():
    meta_path = MODELS_DIR / "latest_model.json"
    if not meta_path.exists():
        raise FileNotFoundError("No model metadata found. Run training first.")
    with open(meta_path, "r", encoding="utf-8") as fh:
        meta = json.load(fh)
    model = joblib.load(meta["model_path"])
    return model, meta


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.get("/model/info")
def model_info() -> dict:
    _, meta = _load_latest_model()
    return meta


@app.post("/forecast", response_model=ForecastResponse)
def forecast(request: ForecastRequest) -> ForecastResponse:
    try:
        model, meta = _load_latest_model()
    except FileNotFoundError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    row = pd.DataFrame([request.model_dump()])[FEATURE_COLUMNS]
    prediction = float(model.predict(row)[0])
    return ForecastResponse(model=meta["model_name"], forecast=prediction)
