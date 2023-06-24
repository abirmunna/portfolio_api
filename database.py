from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

POSTGRESQL_DATABASE_URL = "postgresql+psycopg2://abir:dCucnQWSLZ28WYQLH8t9csGGcQznXLLU@dpg-ciavd4mnqql51cdld0k0-a.singapore-postgres.render.com/portfolio_db_g9bu"


engine = create_engine(
    POSTGRESQL_DATABASE_URL,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

detaSpacekey = "rrMby7BW_PRbjabFY9aUaFrahRoqVf5Kq3c6kCkpf"
