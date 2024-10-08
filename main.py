from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi_login.exceptions import InvalidCredentialsException
from fastapi.middleware.cors import CORSMiddleware
from fastapi_login import LoginManager
from sqlalchemy.orm import Session
import datetime
import os


from fastapi_login.exceptions import InvalidCredentialsException


from business_logic import models, schemas
from database import engine, SessionLocal, get_db
from auth import manager, get_user
from routers import user, about, designation, awards, research, publication, funding, image, cv

# create the database
models.Base.metadata.create_all(bind=engine)

prefix = "/api/v1"

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])



@app.get("/")
def is_aive():
    return {"message": "Hello World"}


@app.post("/login", tags=["Login"])
def login(data: OAuth2PasswordRequestForm = Depends()):
    email = data.username
    pwd = data.password

    user_data = get_user(email)
    if not user_data:
        raise InvalidCredentialsException
    elif pwd != user_data.pwd:
        raise InvalidCredentialsException

    access_token = manager.create_access_token(data={"sub": email}, expires=datetime.timedelta(minutes=3600))
    return {"access_token": access_token}


@app.get("/is_logged_in", tags=["Login"])
def is_logged_in(data: str = Depends(manager)):
    return True


app.include_router(user.router, prefix=prefix)
app.include_router(about.router, prefix=prefix)
app.include_router(designation.router, prefix=prefix)
app.include_router(awards.router, prefix=prefix)
app.include_router(research.router, prefix=prefix)
app.include_router(publication.router, prefix=prefix)
app.include_router(funding.router, prefix=prefix)
app.include_router(image.router, prefix=prefix)
app.include_router(cv.router, prefix=prefix)
