from fastapi import APIRouter, Depends
from business_logic import crud, schemas
from database import SessionLocal, get_db
from auth import manager

router = APIRouter(prefix="/funding", tags=["funding"])


@router.get("/")
def get_funding(db: SessionLocal = Depends(get_db)):
    funding = crud.get_all_funding(db)
    return funding


@router.post("/")
def create_funding(funding: schemas.create_funding, data: str = Depends(manager), db: SessionLocal = Depends(get_db)):
    funding = crud.create_funding(db, funding)
    return funding


@router.put("/")
def update_funding(funding: schemas.funding, data: str = Depends(manager), db: SessionLocal = Depends(get_db)):
    funding = crud.edit_funding(db, funding)
    return funding


@router.delete("/")
def del_funding(id, data: str = Depends(manager), db: SessionLocal = Depends(get_db)):
    funding = crud.delete_funding(db, id)
    return funding
