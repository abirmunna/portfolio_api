from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

# loading test.env from backend directory
load_dotenv("test.env")

POSTGRESQL_DATABASE_URL = os.getenv("DB")

# print(POSTGRESQL_DATABASE_URL)
if POSTGRESQL_DATABASE_URL is None:
    raise ValueError("DB is not set")

engine = create_engine(POSTGRESQL_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# initializing the database in db
def get_db():
    db = SessionLocal()
    try:
        yield db
    except:
        db.close()
