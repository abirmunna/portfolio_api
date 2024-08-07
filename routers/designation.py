from fastapi import APIRouter, Depends
from business_logic import crud, schemas
from database import SessionLocal, get_db
from auth import manager


router = APIRouter()


@router.get("/designation", tags=["designation"])
def get_designation(db: SessionLocal = Depends(get_db)):
    designation = crud.get_all_designations(db)
    return designation


@router.post("/designation", tags=["designation"])
def create_designation(
    designation: schemas.create_designation, data: str = Depends(manager), db: SessionLocal = Depends(get_db)
):
    designation = crud.create_designation(db, designation)
    return designation


@router.put("/designation", tags=["designation"])
def update_designation(
    designation: schemas.designation, data: str = Depends(manager), db: SessionLocal = Depends(get_db)
):
    designation = crud.edit_designation(db, designation)
    return designation


@router.delete("/designation", tags=["designation"])
def del_designation(id, data: str = Depends(manager), db: SessionLocal = Depends(get_db)):
    designation = crud.delete_designation(db, id)
    return designation
