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
    db_about = db.query(models.About).filter(models.About.id == about.id).first()
    db_about.name = about.name
    db_about.motto = about.motto
    db_about.bio = about.bio
    db.commit()
    db.refresh(db_about)
    return db_about

def create_designation(db: Session, designation: schemas.create_designation):
    db_designation = models.Designation(name=designation.name, company=designation.company, location=designation.location)
    db.add(db_designation)
    db.commit()
    db.refresh(db_designation)
    return db_designation

def edit_designation(db: Session, designation: schemas.designation):
    db_designation = db.query(models.Designation).filter(models.Designation.id == designation.id).first()
    db_designation.name = designation.name
    db_designation.company = designation.company
    db_designation.location = designation.location
    db.commit()
    db.refresh(db_designation)
    return db_designation

def delete_designation(db: Session, id: int):
    db_designation = db.query(models.Designation).filter(models.Designation.id == id).first()
    db.delete(db_designation)
    db.commit()
    return db_designation

def get_all_awards(db: Session):
    return db.query(models.Awards).all()

def create_awards(db: Session, awards: schemas.create_awards):
    db_awards = models.Awards(title=awards.title, year=awards.year)
    db.add(db_awards)
    db.commit()
    db.refresh(db_awards)
    return db_awards

def edit_awards(db: Session, awards: schemas.awards):
    db_awards = db.query(models.Awards).filter(models.Awards.id == awards.id).first()
    db_awards.title = awards.title
    db_awards.year = awards.year
    db.commit()
    db.refresh(db_awards)
    return db_awards

def delete_awards(db: Session, id: int):
    db_awards = db.query(models.Awards).filter(models.Awards.id == id).first()
    db.delete(db_awards)
    db.commit()
    return db_awards


def get_all_funding(db: Session):
    return db.query(models.Funding).all()

def create_funding(db: Session, funding: schemas.create_funding):
    db_funding = models.Funding(year=funding.year, title=funding.title, role=funding.role, awarded_amount=funding.awarded_amount, time_period=funding.time_period, doner=funding.doner)
    db.add(db_funding)
    db.commit()
    db.refresh(db_funding)
    return db_funding

def edit_funding(db: Session, funding: schemas.funding):
    db_funding = db.query(models.Funding).filter(models.Funding.id == funding.id).first()
    db_funding.year = funding.year
    db_funding.title = funding.title
    db_funding.role = funding.role
    db_funding.awarded_amount = funding.awarded_amount
    db_funding.time_period = funding.time_period
    db_funding.doner = funding.doner
    db.commit()
    db.refresh(db_funding)
    return db_funding

def delete_funding(db: Session, id: int):
    db_funding = db.query(models.Funding).filter(models.Funding.id == id).first()
    db.delete(db_funding)
    db.commit()
    return db_funding

