from fastapi import APIRouter, Depends
from business_logic import crud, schemas
from database import SessionLocal, get_db


router = APIRouter(prefix="/awards", tags=["awards"])


@router.get("/")
def get_awards(db: SessionLocal = Depends(get_db)):
    awards = crud.get_all_awards(db)
    return awards


@router.post("/")
def create_awards(awards: schemas.create_awards, db: SessionLocal = Depends(get_db)):
    awards = crud.create_awards(db, awards)
    return awards


@router.put("/")
def update_awards(awards: schemas.awards, db: SessionLocal = Depends(get_db)):
    awards = crud.edit_awards(db, awards)
    return awards


@router.delete("/")
def del_awards(id, db: SessionLocal = Depends(get_db)):
    awards = crud.delete_awards(db, id)
    return awards
