# Tests

This folder contains automated checks for core forecasting behavior.

## Current tests

- `test_features.py`: validates feature pipeline output shape and columns.
- `test_api.py`: smoke test for FastAPI health endpoint.

## Run tests

```bash
pytest -q
```

## Scope guidelines

- Add unit tests for feature engineering and metrics first.
- Add integration tests for training outputs and `/forecast` endpoint behavior.
- Keep test data small for fast CI execution.
