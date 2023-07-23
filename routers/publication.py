from fastapi import APIRouter, Depends
from business_logic import crud, schemas
from database import SessionLocal, get_db


router = APIRouter(prefix="/publications", tags=["publications"])


@router.get("/")
def get_publications(db: SessionLocal = Depends(get_db)):
    publications = crud.get_all_publications(db)
    return publications


@router.post("/")
def create_publications(
    publications: schemas.create_publications, db: SessionLocal = Depends(get_db)
):
    publications = crud.create_publications(db, publications)
    return publications


@router.put("/")
def update_publications(
    publications: schemas.publications , db: SessionLocal = Depends(get_db)
):
    publications = crud.edit_publications(db, publications)
    return publications


@router.delete("/")
def del_publications(id, db: SessionLocal = Depends(get_db)):
    publications = crud.delete_publications(db, id)
    return publications
