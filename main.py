from fastapi import FastAPI, Depends, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from fastapi.responses import FileResponse
from fastapi.security import HTTPBasic, HTTPBasicCredentials


from PIL import Image
from io import BytesIO


import crud, models, schemas
from database import SessionLocal, engine

# create the database
models.Base.metadata.create_all(bind=engine)

# not implemented yet
IMAGEDIR = "/images"

app = FastAPI()


app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_methods=["*"]
)  # CORS set to allow all origins and methods


# initializing the database in db
def get_db():
    db = SessionLocal()
    try:
        yield db
    except:
        db.close()


security = HTTPBasic()

def validate_credentials(credentials: HTTPBasicCredentials = Depends(security),db: SessionLocal = Depends(get_db)):
    data = crud.get_user_by_email(db, email=credentials.username)
    if data:
        if data.pwd == credentials.password:
            return data.email
        else:
            return "Not authed"

@app.get("/users/me")
async def read_current_user(username: str = Depends(validate_credentials)):
    return {"message": username}


@app.get("/")
def index():
    return {"message": "Hello World"}

@app.get("/user", tags=["user"])
def get_all_user(db: SessionLocal = Depends(get_db)):
    return crud.get_all_user(db=db)

@app.post("/user", tags=["user"])
def create_user(user: schemas.user, db: SessionLocal = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        return {"message": "Email already registered"}
    return crud.create_user(db=db, user=user)

@app.put("/user", tags=["user"])
def edit_user(user: schemas.user, db: SessionLocal = Depends(get_db),login: str = Depends(validate_credentials)):
    return crud.edit_user(db=db, user=user)

@app.delete("/user", tags=["user"])
def delete_user(user: schemas.user, db: SessionLocal = Depends(get_db),login: str = Depends(validate_credentials)):
    return crud.delete_user(db=db, user=user)

# @app.post("/login", tags=["user"])
# def login_user(user: schemas.user, db: SessionLocal = Depends(get_db)):
#     return crud.login_user(db=db, user=user)

"""
    About Section starts here
    This section is for the about me section of the website
    -routes:
        -/about(GET): returns the about me section
        -/about(PUT): edits the about me section
"""


@app.get("/about", tags=["about"])
def about_me(db: SessionLocal = Depends(get_db)):
    about = crud.get_about(db)
    return about


# only for dev use
# @app.post('/about')
# def about_me(about: schemas.about, db: SessionLocal = Depends(get_db)):
#     about = crud.create_about(db, about)
#     return about


@app.put("/about", tags=["about"])
def about_me(about: schemas.about, db: SessionLocal = Depends(get_db),username: str = Depends(validate_credentials)):
    about = crud.edit_about(db, about)
    return about


"""
    Designation Section starts here

    -routes:
        -/designation(GET): returns all the designations
        -/designation(POST): creates a new designation
        -/designation(PUT): edits a designation
        -/designation(DELETE): deletes a designation
"""


@app.get("/designation", tags=["designation"])
def designation(db: SessionLocal = Depends(get_db)):
    designation = crud.get_all_designations(db)
    return designation


@app.post("/designation", tags=["designation"])
def designation(
    designation: schemas.create_designation, db: SessionLocal = Depends(get_db),
    username: str = Depends(validate_credentials)
):
    designation = crud.create_designation(db, designation)
    return designation


@app.put("/designation", tags=["designation"])
def designation(designation: schemas.designation, db: SessionLocal = Depends(get_db),username: str = Depends(validate_credentials)):
    designation = crud.edit_designation(db, designation)
    return designation


@app.delete("/designation", tags=["designation"])
def designation(id, db: SessionLocal = Depends(get_db), username: str = Depends(validate_credentials)):
    designation = crud.delete_designation(db, id)
    return designation


# picture section(Not implemented yet)
# @app.post("/upload/", tags=["picture"])
# async def create_upload_file(file: UploadFile = File(...)):
#     file.filename = f"profile.jpg"
#     contents = await file.read()

#     # save the file
#     with open(f"{IMAGEDIR}{file.filename}", "wb") as f:
#         f.write(contents)

#     return {"filename": file.filename}


# @app.get("/image", tags=["picture"])
# def get_image():
#     image_path = "tmp/images/profile.jpg"  # Replace with the actual path to your image
#     img = Image.open(image_path)
#     img_byte_arr = BytesIO()
#     img.save(img_byte_arr, format="JPEG")
#     img_byte_arr.seek(0)
#     return StreamingResponse(img_byte_arr, media_type="image/jpeg")

"""
    Awards Section starts here
    -routes:
        -/awards(GET): returns all the awards
        -/awards(POST): creates a new award
        -/awards(PUT): edits a award
        -/awards(DELETE): deletes a award
"""


@app.get("/awards", tags=["awards"])
def awards(db: SessionLocal = Depends(get_db)):
    awards = crud.get_all_awards(db)
    return awards


@app.post("/awards", tags=["awards"])
def awards(awards: schemas.create_awards, db: SessionLocal = Depends(get_db),username: str = Depends(validate_credentials)):
    awards = crud.create_awards(db, awards)
    return awards


@app.put("/awards", tags=["awards"])
def awards(awards: schemas.awards, db: SessionLocal = Depends(get_db),username: str = Depends(validate_credentials)):
    awards = crud.edit_awards(db, awards)
    return awards


@app.delete("/awards", tags=["awards"])
def awards(id, db: SessionLocal = Depends(get_db),username: str = Depends(validate_credentials)):
    awards = crud.delete_awards(db, id)
    return awards


"""
    Funding Section starts here
    -routes:
        -/funding(GET): returns all the funding
        -/funding(POST): creates a new funding
        -/funding(PUT): edits a funding
        -/funding(DELETE): deletes a funding
"""


@app.get("/funding", tags=["funding"])
def funding(db: SessionLocal = Depends(get_db)):
    funding = crud.get_all_funding(db)
    return funding


@app.post("/funding", tags=["funding"])
def funding(funding: schemas.create_funding, db: SessionLocal = Depends(get_db),username: str = Depends(validate_credentials)):
    funding = crud.create_funding(db, funding)
    return funding


@app.put("/funding", tags=["funding"])
def funding(funding: schemas.funding, db: SessionLocal = Depends(get_db),username: str = Depends(validate_credentials)):
    funding = crud.edit_funding(db, funding)
    return funding


@app.delete("/funding", tags=["funding"])
def funding(id, db: SessionLocal = Depends(get_db), username: str = Depends(validate_credentials)):
    funding = crud.delete_funding(db, id)
    return funding


@app.get("/research", tags=["research"], response_model=list[schemas.research])
def research(db: SessionLocal = Depends(get_db)):
    research = crud.get_all_research(db)
    return research


@app.post("/research", tags=["research"])
def research(research: schemas.create_research, db: SessionLocal = Depends(get_db),username: str = Depends(validate_credentials)):
    research = crud.create_research(db, research)
    return research


@app.put("/research", tags=["research"])
def research(research: schemas.research, db: SessionLocal = Depends(get_db),username: str = Depends(validate_credentials)):
    research = crud.edit_research(db, research)
    return research


@app.delete("/research", tags=["research"])
def research(id, db: SessionLocal = Depends(get_db),username: str = Depends(validate_credentials)):
    research = crud.delete_research(db, id)
    return research


@app.get("/publications", tags=["publications"])
def publications(db: SessionLocal = Depends(get_db)):
    publications = crud.get_all_publications(db)
    return publications


@app.post("/publications", tags=["publications"])
def publications(
    publications: schemas.create_publications, db: SessionLocal = Depends(get_db),
    username: str = Depends(validate_credentials)
):
    publications = crud.create_publications(db, publications)
    return publications


@app.put("/publications", tags=["publications"])
def publications(
    publications: schemas.create_publications, db: SessionLocal = Depends(get_db),
    username: str = Depends(validate_credentials)
):
    publications = crud.edit_publications(db, publications)
    return publications


@app.delete("/publications", tags=["publications"])
def publications(id, db: SessionLocal = Depends(get_db),username: str = Depends(validate_credentials)):
    publications = crud.delete_publications(db, id)
    return publications
