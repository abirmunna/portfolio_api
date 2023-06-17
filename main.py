from fastapi import FastAPI, Depends, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from fastapi.responses import FileResponse

from PIL import Image
from io import BytesIO

import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)
IMAGEDIR = "images/"

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*'],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    except:
        db.close()

@app.get('/')
def index():
    return {'message': 'Hello World'}
# about me section
@app.get('/about', tags=['about'])
def about_me(db: SessionLocal = Depends(get_db)):
    about = crud.get_about(db)
    return about

# @app.post('/about')
# def about_me(about: schemas.about, db: SessionLocal = Depends(get_db)):
#     about = crud.create_about(db, about)
#     return about

@app.put('/about', tags=['about'])
def about_me(about: schemas.about, db: SessionLocal = Depends(get_db)):
    about = crud.edit_about(db, about)
    return about

# designation section
@app.get('/designation', tags=['designation'])
def designation(db: SessionLocal = Depends(get_db)):
    designation = crud.get_all_designations(db)
    return designation

@app.post('/designation', tags=['designation'])
def designation(designation: schemas.create_designation, db: SessionLocal = Depends(get_db)):
    designation = crud.create_designation(db, designation)
    return designation

@app.put('/designation', tags=['designation'])
def designation(designation: schemas.designation, db: SessionLocal = Depends(get_db)):
    designation = crud.edit_designation(db, designation)
    return designation

@app.delete('/designation', tags=['designation'])
def designation(id, db: SessionLocal = Depends(get_db)):
    designation = crud.delete_designation(db, id)
    return designation

# picture section
@app.post("/upload/", tags=['picture'])
async def create_upload_file(file: UploadFile = File(...)):
 
    file.filename = f"profile.jpg"
    contents = await file.read()
 
    #save the file
    with open(f"{IMAGEDIR}{file.filename}", "wb") as f:
        f.write(contents)
 
    return {"filename": file.filename}


@app.get("/image", tags=['picture'])
def get_image():
    image_path = "images/profile.jpg"  # Replace with the actual path to your image
    img = Image.open(image_path)
    img_byte_arr = BytesIO()
    img.save(img_byte_arr, format='JPEG')
    img_byte_arr.seek(0)
    return StreamingResponse(img_byte_arr, media_type="image/jpeg")


@app.get("/awards", tags=['awards'])
def awards(db: SessionLocal = Depends(get_db)):
    awards = crud.get_all_awards(db)
    return awards

@app.post("/awards", tags=['awards'])
def awards(awards: schemas.create_awards, db: SessionLocal = Depends(get_db)):
    awards = crud.create_awards(db, awards)
    return awards

@app.put("/awards", tags=['awards'])
def awards(awards: schemas.awards, db: SessionLocal = Depends(get_db)):
    awards = crud.edit_awards(db, awards)
    return awards

@app.delete("/awards", tags=['awards'])
def awards(id, db: SessionLocal = Depends(get_db)):
    awards = crud.delete_awards(db, id)
    return awards

@app.get("/funding", tags=['funding'])
def funding(db: SessionLocal = Depends(get_db)):
    funding = crud.get_all_funding(db)
    return funding

@app.post("/funding", tags=['funding'])
def funding(funding: schemas.create_funding, db: SessionLocal = Depends(get_db)):
    funding = crud.create_funding(db, funding)
    return funding

@app.put("/funding", tags=['funding'])
def funding(funding: schemas.funding, db: SessionLocal = Depends(get_db)):
    funding = crud.edit_funding(db, funding)
    return funding

@app.delete("/funding", tags=['funding'])
def funding(id, db: SessionLocal = Depends(get_db)):
    funding = crud.delete_funding(db, id)
    return funding

