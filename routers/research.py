from fastapi import APIRouter, Depends
from business_logic import crud, schemas
from database import SessionLocal, get_db
from auth import manager


router = APIRouter(prefix="/research", tags=["research"])


@router.get("/", response_model=list[schemas.research])
def get_research(db: SessionLocal = Depends(get_db)):
    research = crud.get_all_research(db)
    return research


@router.post("/")
def create_research(
    research: schemas.create_research, data: str = Depends(manager), db: SessionLocal = Depends(get_db)
):
    research = crud.create_research(db, research)
    return research


@router.put("/")
def update_research(research: schemas.research, data: str = Depends(manager), db: SessionLocal = Depends(get_db)):
    research = crud.edit_research(db, research)
    return research


@router.delete("/")
def del_research(id, data: str = Depends(manager), db: SessionLocal = Depends(get_db)):
    research = crud.delete_research(db, id)
    return research
