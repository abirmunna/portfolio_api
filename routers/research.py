from fastapi import APIRouter, Depends
from business_logic import crud, schemas
from database import SessionLocal, get_db
from main import manager


router = APIRouter(prefix="/research", tags=["research"])


@router.get("/", response_model=list[schemas.research])
def get_research(db: SessionLocal = Depends(get_db)):
    research = crud.get_all_research(db)
    return research


@router.post("/")
def create_research(
    research: schemas.create_research, db: SessionLocal = Depends(get_db), dependencies=[Depends(manager)]
):
    research = crud.create_research(db, research)
    return research


@router.put("/")
def update_research(research: schemas.research, db: SessionLocal = Depends(get_db), dependencies=[Depends(manager)]):
    research = crud.edit_research(db, research)
    return research


@router.delete("/")
def del_research(id, db: SessionLocal = Depends(get_db), dependencies=[Depends(manager)]):
    research = crud.delete_research(db, id)
    return research
