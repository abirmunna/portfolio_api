from fastapi import APIRouter, File, UploadFile
from fastapi.responses import HTMLResponse
from deta import Deta

deta = Deta()
db = deta.Drive("t")

router = APIRouter(prefix="/image", tags=["image"])


@router.get("/get_all")
def get_all_image_names():
    return db.list()["names"]


@router.get("/uploads/{filename}")
def get_image(filename: str):
    file = db.get(filename)
    content = file.read()
    return HTMLResponse(content, media_type="image/png")


@router.post("/uploads")
def upload_image(file: UploadFile = File(...)):
    # if not png conever to png
    if file.content_type != "image/png":
        # convert to png
        filename = file.filename.split(".")[0] + ".png"
        db.put(filename, file.file)
        return {"File uploaded successfully": filename}
    else:
        db.put(file.filename, file.file)
        return {"File uploaded successfully": file.filename}
