# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, declarative_base
# from business_logic import models
# import dotenv
# import os

# dotenv.load_dotenv("test.env")

# db = os.getenv("DB")


# # print(POSTGRESQL_DATABASE_URL)
# if db is None:
#     raise ValueError("DB is not set")

# engine = create_engine(db)

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base()

# db = SessionLocal()
