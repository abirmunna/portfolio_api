from fastapi import APIRouter, File, UploadFile
from fastapi.responses import HTMLResponse
from deta import Deta

deta = Deta()
db = deta.Drive("t")

router = APIRouter(prefix="/cv", tags=["cv"])

@router.get("/get_all")
def get_all_cv_names():
    return db.list()["names"]

@router.get("/uploads/{filename}")
def get_cv(filename: str):
    file = db.get(filename)
    content = file.read()
    return HTMLResponse(content, media_type="application/pdf")

@router.post("/uploads")
def upload_cv(file: UploadFile = File(...)):
    # if not pdf conevert to pdf
    if file.content_type != "application/pdf":
        # convert to pdf
        filename = file.filename.split(".")[0] + ".pdf"
        db.put(filename, file.file)
        return {"File uploaded successfully": filename}
    else:
        db.put(file.filename, file.file)
        return {"File uploaded successfully": file.filename}