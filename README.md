# End To End Forecasting (In Progress)

## Objective
Build a machine learning system that forecasts product demand to support inventory planning.

## Input
- Historical sales data
- Product ID
- Store or region
- Calendar features (day, week, month)
- Promotions

## Output
Demand forecast for the next 4–8 weeks.\
Example:
```
{
  "product_id": 1423,
  "store_id": 5,
  "forecast": [120, 135, 140, 160]
}
```

## Dataset
[Store Item Demand Forecasting Challenge Dataset](https://www.kaggle.com/datasets/dhrubangtalukdar/store-item-demand-forecasting-dataset)
