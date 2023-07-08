from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from business_logic import models
from database import engine
from routers import user, about, designation, awards, research, publication, funding

# create the database
models.Base.metadata.create_all(bind=engine)

IMAGEDIR = "/images"

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"])

app.include_router(user.router)
app.include_router(about.router)
app.include_router(designation.router)
app.include_router(awards.router)
app.include_router(research.router)
app.include_router(publication.router)
app.include_router(funding.router)


@app.get("/")
def is_aive():
    return {"message": "Hello World"}
