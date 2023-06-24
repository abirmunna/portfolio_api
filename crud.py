from sqlalchemy.orm import Session
import models, schemas


def create_user(db: Session, user: schemas.user):
    db_user = models.User(email=user.email, pwd=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user) 
    return db_user

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def edit_user(db: Session, user: schemas.user):
    db_user = db.query(models.User).filter(models.User.id == 1).first()
    update_data = user.dict(exclude_unset=True)
    db.query(models.User).filter(models.User.id == 1).update(
        update_data, synchronize_session=False
    )
    db.commit()
    db.refresh(db_user)
    return db_user


def login_user(db: Session, user: schemas.user):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user.pwd == user.pwd:
        return db_user
    else:
        return None



def get_about(db: Session):
    return db.query(models.About).all()


def create_about(db: Session, about: schemas.about):
    db_about = models.About(name=about.name, motto=about.motto, bio=about.bio)
    db.add(db_about)
    db.commit()
    db.refresh(db_about)
    return db_about


def edit_about(db: Session, about: schemas.about):
    db_about = db.query(models.About).filter(models.About.id == about.id).first()
    update_data = about.dict(exclude_unset=True)
    db.query(models.About).filter(models.About.id == about.id).update(
        update_data, synchronize_session=False
    )
    db.commit()
    db.refresh(db_about)
    return db_about


def get_all_designations(db: Session):
    # return in ascending order
    return db.query(models.Designation).order_by(models.Designation.id.desc()).all()


def create_designation(db: Session, designation: schemas.create_designation):
    db_designation = models.Designation(
        name=designation.name,
        company=designation.company,
        location=designation.location,
    )
    db.add(db_designation)
    db.commit()
    db.refresh(db_designation)
    return db_designation


def edit_designation(db: Session, designation: schemas.designation):
    db_designation = (
        db.query(models.Designation)
        .filter(models.Designation.id == designation.id)
        .first()
    )
    update_data = designation.dict(exclude_unset=True)
    db.query(models.Designation).filter(models.Designation.id == designation.id).update(
        update_data, synchronize_session=False
    )
    db.commit()
    db.refresh(db_designation)
    return db_designation


def delete_designation(db: Session, id: int):
    db_designation = (
        db.query(models.Designation).filter(models.Designation.id == id).first()
    )
    db.delete(db_designation)
    db.commit()
    return db_designation


def get_all_awards(db: Session):
    return db.query(models.Awards).order_by(models.Awards.id.desc()).all()


def create_awards(db: Session, awards: schemas.create_awards):
    db_awards = models.Awards(title=awards.title, year=awards.year)
    db.add(db_awards)
    db.commit()
    db.refresh(db_awards)
    return db_awards


def edit_awards(db: Session, awards: schemas.awards):
    db_awards = db.query(models.Awards).filter(models.Awards.id == awards.id).first()
    update_data = awards.dict(exclude_unset=True)
    db.query(models.Awards).filter(models.Awards.id == awards.id).update(
        update_data, synchronize_session=False
    )
    db.commit()
    db.refresh(db_awards)
    return db_awards


def delete_awards(db: Session, id: int):
    db_awards = db.query(models.Awards).filter(models.Awards.id == id).first()
    db.delete(db_awards)
    db.commit()
    return db_awards


def get_all_funding(db: Session):
    return db.query(models.Funding).order_by(models.Funding.id.desc()).all()


def create_funding(db: Session, funding: schemas.create_funding):
    db_funding = models.Funding(
        year=funding.year,
        title=funding.title,
        role=funding.role,
        awarded_amount=funding.awarded_amount,
        time_period=funding.time_period,
        doner=funding.doner,
    )
    db.add(db_funding)
    db.commit()
    db.refresh(db_funding)
    return db_funding


def edit_funding(db: Session, funding: schemas.funding):
    db_funding = (
        db.query(models.Funding).filter(models.Funding.id == funding.id).first()
    )
    update_data = funding.dict(exclude_unset=True)
    db.query(models.Funding).filter(models.Funding.id == funding.id).update(
        update_data, synchronize_session=False
    )
    db.commit()
    db.refresh(db_funding)
    return db_funding


def delete_funding(db: Session, id: int):
    db_funding = db.query(models.Funding).filter(models.Funding.id == id).first()
    db.delete(db_funding)
    db.commit()
    return db_funding


def get_all_research(db: Session):
    return db.query(models.Research).order_by(models.Research.id.desc()).all()


def create_research(db: Session, research: schemas.create_research):
    db_research = models.Research(
        title=research.title,
        description=research.description,
    )
    db.add(db_research)
    db.commit()
    db.refresh(db_research)
    return db_research


def edit_research(db: Session, research: schemas.research):
    db_research = (
        db.query(models.Research).filter(models.Research.id == research.id).first()
    )
    
    update_data = research.dict(exclude_unset=True)
    db.query(models.Research).filter(models.Research.id == research.id).update(
        update_data, synchronize_session=False
    )
    db.commit()
    db.refresh(db_research)
    return db_research


def delete_research(db: Session, id: int):
    db_research = db.query(models.Research).filter(models.Research.id == id).first()
    db.delete(db_research)
    db.commit()
    return db_research


def get_all_publications(db: Session):
    return db.query(models.Publications).order_by(models.Publications.id.desc()).all()


def create_publications(db: Session, publications: schemas.create_publications):
    db_publications = models.Publications(
        title=publications.title,
        published=publications.published,
        authors=publications.authors,
        research_id=publications.research_id,
    )

    db.add(db_publications)
    db.commit()
    db.refresh(db_publications)
    return db_publications


def edit_publications(db: Session, publications: schemas.publications):
    db_publications = (
        db.query(models.Publications)
        .filter(models.Publications.id == publications.id)
        .first()
    )
    update_data = publications.dict(exclude_unset=True)
    db.query(models.Publications).filter(
        models.Publications.id == publications.id
    ).update(update_data, synchronize_session=False)
    db.commit()
    db.refresh(db_publications)
    return db_publications


def delete_publications(db: Session, id: int):
    db_publications = (
        db.query(models.Publications).filter(models.Publications.id == id).first()
    )
    db.delete(db_publications)
    db.commit()
    return db_publications
