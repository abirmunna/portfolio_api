from sqlalchemy import Integer, String, Column, Boolean, ForeignKey
from sqlalchemy.orm import relationship

import sys
sys.path.append("..")
from database import Base


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255))
    pwd = Column(String(255))


class Token(Base):
    __tablename__ = "token"
    id = Column(Integer, primary_key=True, index=True)
    access_token = Column(String(255))
    token_type = Column(String(255))


class About(Base):
    __tablename__ = "about"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    motto = Column(String(255))
    bio = Column(String(255))


class Designation(Base):
    __tablename__ = "designation"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    company = Column(String(255))
    location = Column(String(255))


class Awards(Base):
    __tablename__ = "awards"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    year = Column(String(255))


class Funding(Base):
    __tablename__ = "funding"
    id = Column(Integer, primary_key=True, index=True)
    year = Column(String(255))
    title = Column(String(255))
    role = Column(String(255))
    awarded_amount = Column(String(255))
    time_period = Column(String(255))
    doner = Column(String(255))


class Research(Base):
    __tablename__ = "research"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    description = Column(String(255))

    publications = relationship("Publications", back_populates="research")


class Publications(Base):
    __tablename__ = "publications"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    published = Column(String(255))
    authors = Column(String(255))
    research_id = Column(Integer, ForeignKey("research.id"))

    research = relationship("Research", back_populates="publications")
