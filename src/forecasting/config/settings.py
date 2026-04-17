from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[3]
DATA_DIR = ROOT_DIR / "dataset"
ARTIFACTS_DIR = ROOT_DIR / "artifacts"
MODELS_DIR = ARTIFACTS_DIR / "models"
METRICS_DIR = ARTIFACTS_DIR / "metrics"

DEFAULT_TARGET_COL = "sales"
DEFAULT_DATE_COL = "date"
DEFAULT_ID_COLS = ["store", "item"]
