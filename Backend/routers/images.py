from fastapi import APIRouter, UploadFile, File, Depends
from pathlib import Path
import shutil
from auth import authenticate

router = APIRouter(
    prefix="/images",
    tags=["Images"],
    dependencies=[Depends(authenticate)]
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