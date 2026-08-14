import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def fetch_image_url(nikke_page_url):
    soup = fetch(nikke_page_url)  # reuse polite fetch function
    if not soup:
        return None
    # Find infobox image (usually first image in a table with class "infobox")
    img = soup.select_one("table.infobox img")
    if img and img.get("src"):
        return img["src"]
    # Fallback: any large image
    img2 = soup.find("img", {"width": True, "height": True})
    return img2.get("src") if img2 else None

def download_image(img_url, save_dir, name):
    try:
        resp = requests.get(img_url, stream=True)
        resp.raise_for_status()
        ext = os.path.splitext(img_url)[1].split('?')[0] or '.jpg'
        safe = "".join(c if c.isalnum() else "_" for c in name)
        path = os.path.join(save_dir, f"{safe}{ext}")
        with open(path, 'wb') as f:
            for chunk in resp.iter_content(1024):
                f.write(chunk)
        return path
    except Exception as e:
        print(f"[warn] Error saving image {img_url}: {e}")
        return None
