# path.py
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
# print(BASE_DIR)
SCR_DIR = BASE_DIR / "src"
DATA_DIR = BASE_DIR / "data"
ASSETS_DIR = BASE_DIR.parent / "assets"
OUTPUTS_DIR = BASE_DIR.parent / "outputs"

PDF_DIR = OUTPUTS_DIR  / "pdf"

FONTS_DIR = ASSETS_DIR / "fonts"

AGREEMENT_FILE = DATA_DIR / "is_agreed.txt"
LOG_FILE = DATA_DIR / "logs.txt"
