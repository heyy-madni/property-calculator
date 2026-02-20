# walk.py
from pathlib import Path
import sys

if getattr(sys, 'frozen', False):
    # Running inside PyInstaller EXE
    BASE_DIR = Path(sys._MEIPASS)
else:
    # Running as normal Python script
    BASE_DIR = Path(__file__).resolve().parent.parent

SCR_DIR = BASE_DIR / "src"
DATA_DIR = BASE_DIR / "data"
ASSETS_DIR = BASE_DIR / "assets"
OUTPUTS_DIR = BASE_DIR / "outputs"

PDF_DIR = OUTPUTS_DIR / "pdf"
FONTS_DIR = ASSETS_DIR / "fonts"

AGREEMENT_FILE = DATA_DIR / "is_agreed.txt"
LOG_FILE = DATA_DIR / "logs.txt"
