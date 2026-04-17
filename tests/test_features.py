import pandas as pd

from forecasting.features.pipeline import FEATURE_COLUMNS, prepare_training_matrix


def test_prepare_training_matrix_has_expected_columns():
    df = pd.DataFrame(
        {
            "date": pd.date_range("2024-01-01", periods=20, freq="D"),
            "store": [1] * 20,
            "item": [10] * 20,
            "promo": [0, 1] * 10,
            "sales": [float(v) for v in range(20)],
        }
    )
    X, y = prepare_training_matrix(df)
    assert list(X.columns) == FEATURE_COLUMNS
    assert len(X) == len(y)
