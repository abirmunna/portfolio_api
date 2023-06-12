from sqlalchemy.orm import Session
import models, schemas

def get_about(db: Session):
    return db.query(models.About).all()

def get_all_designations(db: Session):
    return db.query(models.Designation).all()

def create_about(db: Session, about: schemas.about):
    db_about = models.About(name=about.name, motto=about.motto, bio=about.bio)
    db.add(db_about)
    db.commit()
    db.refresh(db_about)
    return db_about

def edit_about(db: Session, about: schemas.about):
    db_about = db.query(models.About).filter(models.About.name == about.name).first()
    db_about.name = about.name
    db_about.motto = about.motto
    db_about.bio = about.bio
    db.commit()
    db.refresh(db_about)
    return db_about

def create_designation(db: Session, designation: schemas.designation):
    db_designation = models.Designation(name=designation.name, company=designation.company, location=designation.location)
    db.add(db_designation)
    db.commit()
    db.refresh(db_designation)
    return db_designation

def edit_designation(id: int ,db: Session, designation: schemas.designation):
    db_designation = db.query(models.Designation).filter(models.Designation.id == id).first()
    db_designation.name = designation.name
    db_designation.company = designation.company
    db_designation.location = designation.location
    db.commit()
    db.refresh(db_designation)
    return db_designation

def delete_designation(id: int, db: Session):
    db_designation = db.query(models.Designation).filter(models.Designation.id == id).first()
    db.delete(db_designation)
    db.commit()
    return db_designation