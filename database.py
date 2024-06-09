from sqlalchemy import create_engine, MetaData, text
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

# loading test.env from backend directory
load_dotenv(".env")

POSTGRESQL_DATABASE_URL = os.getenv("DB")

# print(POSTGRESQL_DATABASE_URL)
if POSTGRESQL_DATABASE_URL is None:
    raise ValueError("DB is not set")

engine = create_engine(POSTGRESQL_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
# Session = SessionLocal()
# Add the new column to the table
# Session.execute(text('ALTER TABLE research ADD COLUMN status VARCHAR(255)'))
# Session.execute(text('ALTER TABLE publications ADD COLUMN publications_type VARCHAR(255)'))
# Session.execute(text('ALTER TABLE publications ADD COLUMN url VARCHAR(25500)'))
# alter the string size for About table motto column
# Session.execute(text('ALTER TABLE about ALTER COLUMN bio TYPE VARCHAR(25500)'))
# Session.execute(text('ALTER TABLE research ALTER COLUMN description TYPE VARCHAR(25500)'))
# Commit the changes
# Session.commit()



# initializing the database in db
def get_db():
    db = SessionLocal()
    try:
        yield db
    except:
        db.close()
