from __future__ import annotations

import json
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st


st.title("Demand Forecasting Dashboard")

metrics_dir = Path("artifacts/metrics")
reports = sorted(metrics_dir.glob("training_report_*.json"))
if not reports:
    st.warning("No training reports found. Run training first.")
    st.stop()

with open(reports[-1], "r", encoding="utf-8") as fh:
    report = json.load(fh)

st.subheader("Champion Model")
st.write(report["champion_model"])

df = pd.DataFrame(report["metrics"])
st.subheader("Model Comparison")
st.dataframe(df)

metric_name = st.selectbox("Metric", ["mae", "rmse", "mape"], index=1)
fig = px.bar(df, x="model", y=metric_name, title=f"Backtesting {metric_name.upper()}")
st.plotly_chart(fig, use_container_width=True)
