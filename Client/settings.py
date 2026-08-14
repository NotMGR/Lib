import json
import os
from pathlib import Path


CONFIG_DIR = Path(os.getenv("APPDATA", Path.home())) / "Lib"
CONFIG_PATH = CONFIG_DIR / "config.json"


def get_base_url():
    return load_config().get("server", "").rstrip("/")

def load_config():
    if not CONFIG_PATH.exists():
        return {}

    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def save_config(config):
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)

    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=4)