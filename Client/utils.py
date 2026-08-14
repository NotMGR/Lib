from pathlib import Path
import sys

if getattr(sys, "frozen", False):
    BASE_DIR = Path(sys._MEIPASS)
else:
    BASE_DIR = Path(__file__).resolve().parent

def resource_path(relative_path):    
    return BASE_DIR / relative_path

def nikke_image(filename: str) -> Path:
    return resource_path(f"images/nikkes/{filename}")