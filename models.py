from sqlalchemy import Integer, String, Column, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class About(Base):
    __tablename__ = "about"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    motto = Column(String, unique=True, index=True)
    bio = Column(String, unique=True, index=True)

class Designation(Base):
    __tablename__ = "designation"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    company = Column(String, unique=True, index=True)
    location = Column(String, unique=True, index=True)

class Awards(Base):
    __tablename__ = "awards"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)
    year = Column(String, unique=True, index=True)


class Funding(Base):
    __tablename__ = "funding"
    id = Column(Integer, primary_key=True, index=True)
    year = Column(String, unique=True, index=True)
    title = Column(String, unique=True, index=True)
    role = Column(String, unique=True, index=True)
    awarded_amount = Column(String, unique=True, index=True)
    time_period = Column(String, unique=True, index=True)
    doner = Column(String, unique=True, index=True)