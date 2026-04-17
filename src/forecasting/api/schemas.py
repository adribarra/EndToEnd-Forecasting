from __future__ import annotations

from pydantic import BaseModel, Field


class ForecastRequest(BaseModel):
    store: int = Field(..., ge=1)
    item: int = Field(..., ge=1)
    promo: int = Field(default=0, ge=0, le=1)
    lag_1: float
    lag_7: float
    rolling_mean_7: float
    day_of_week: int = Field(..., ge=0, le=6)
    month: int = Field(..., ge=1, le=12)
    week_of_year: int = Field(..., ge=1, le=53)
    is_weekend: int = Field(..., ge=0, le=1)


class ForecastResponse(BaseModel):
    model: str
    forecast: float
