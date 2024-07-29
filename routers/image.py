from fastapi import APIRouter, File, UploadFile
from fastapi.responses import FileResponse
import os

router = APIRouter(prefix="/image", tags=["image"])

IMAGEDIR = "/home/ubuntu/portfolio_api/images"
@router.get("/get_all")
def get_all_image_names():
    return os.listdir(IMAGEDIR)


@router.get("/uploads/{filename}")
def get_image(filename: str):
    return FileResponse(os.path.join(IMAGEDIR, filename))


@router.post("/uploads")
def upload_image(file: UploadFile = File(...)):
    filename = file.filename
    with open(os.path.join(IMAGEDIR, filename), "wb") as f:
        f.write(file.file.read())
    return {"filename": filename}
