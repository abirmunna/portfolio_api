from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv, find_dotenv
import dotenv
import os

load_dotenv('test.env')

POSTGRESQL_DATABASE_URL = os.getenv("DB")

print(POSTGRESQL_DATABASE_URL)
engine = create_engine(
    POSTGRESQL_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

