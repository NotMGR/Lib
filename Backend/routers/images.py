from fastapi import APIRouter, UploadFile, File
from pathlib import Path
import shutil

router = APIRouter(
    prefix="/images",
    tags=["Images"]
)

IMAGE_FOLDER = Path("images/nikke")

@router.post("/nikke")
def upload_nikke_image(
    image: UploadFile = File(...)
):
    destination = IMAGE_FOLDER / image.filename

    with destination.open("wb") as buffer:
        shutil.copyfileobj(
            image.file,
            buffer
        )

    return {
        "image_path": f"{image.filename}"
    }