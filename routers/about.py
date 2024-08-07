from fastapi import APIRouter, Depends
from business_logic import crud, schemas
from database import SessionLocal, get_db
from auth import manager

router = APIRouter(prefix="/about", tags=["about"])


@router.get("/")
def get_about_me(db: SessionLocal = Depends(get_db)):
    about = crud.get_about(db=db)
    return about


# only for dev use
# @router.post("/")
# def about_me(about: schemas.about, db: SessionLocal = Depends(get_db)):
#     about = crud.create_about(db, about)
#     return about


@router.put("/")
def update_about_me(about: schemas.about, data: str = Depends(manager), db: SessionLocal = Depends(get_db)):
    if crud.get_about(db=db) is None:
        raise ValueError("About me is not set")

    about = crud.edit_about(db, about)
    return about
