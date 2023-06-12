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