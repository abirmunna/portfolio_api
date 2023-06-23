from sqlalchemy import create_engine 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker 
 
MYSQL_DATABASE_URL= "mysql+mysqlconnector://sql12628181:caL2G6bsgb@sql12.freemysqlhosting.net:3306/sql12628181"


engine = create_engine(
    MYSQL_DATABASE_URL,
    )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

mykey = "rrMby7BW_PRbjabFY9aUaFrahRoqVf5Kq3c6kCkpf"