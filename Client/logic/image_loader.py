from pathlib import Path

import requests

from settings import get_base_url
from PySide6.QtGui import QPixmap


CACHE_DIR = Path("cache/images")
CACHE_DIR.mkdir(parents=True, exist_ok=True)

def cache_path(image_path: str):
    path = CACHE_DIR / image_path

    path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    return path

def get_pixmap(image_path):
    local = cache_path(image_path)

    if not local.exists():
        url = f"{get_base_url()}/images/{image_path}"

        response = requests.get(url)

        response.raise_for_status()

        local.write_bytes(response.content)

    return QPixmap(str(local))