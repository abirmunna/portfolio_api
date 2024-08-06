from fastapi import APIRouter, File, UploadFile
from fastapi.responses import FileResponse
import os
from main import manager

CVDIR = "/home/ubuntu/portfolio_api/cv"

router = APIRouter(prefix="/cv", tags=["cv"])

@router.get("/get_all")
def get_all_cv_names():
    return os.listdir(CVDIR)

@router.get("/uploads/{filename}")
def get_cv(filename: str):
    return FileResponse(os.path.join(CVDIR, filename))

@router.post("/uploads", dependencies=[Depends(manager)])
def upload_cv(file: UploadFile = File(...)):
    filename = file.filename
    with open(os.path.join(CVDIR, filename), "wb") as f:
        f.write(file.file.read())
