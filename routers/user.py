from fastapi import APIRouter, Depends
from business_logic import crud, schemas
from database import SessionLocal, get_db
from auth import manager

router = APIRouter()


@router.get("/user", tags=["user"])
def get_all_user(db: SessionLocal = Depends(get_db)):
    return crud.get_all_user(db=db)


@router.post("/user", tags=["user"])
def create_user(user: schemas.user, db: SessionLocal = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        return {"message": "Email already registered"}
    return crud.create_user(db=db, user=user)


@router.put("/user", tags=["user"])
def edit_user(user: schemas.user, data: str = Depends(manager), db: SessionLocal = Depends(get_db)):
    return crud.edit_user(db=db, user=user)


@router.delete("/user", tags=["user"])
def delete_user(user: schemas.user, data: str = Depends(manager), db: SessionLocal = Depends(get_db)):
    return crud.delete_user(db=db, user=user)
