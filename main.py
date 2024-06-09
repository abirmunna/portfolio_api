from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from business_logic import models
from database import engine
from routers import user, about, designation, awards, research, publication, funding

# create the database
models.Base.metadata.create_all(bind=engine)

IMAGEDIR = "/images"
prefix = "/api/v1"

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"])


@app.get("/")
def is_aive():
    return {"message": "Hello World"}


app.include_router(user.router, prefix=prefix)
app.include_router(about.router, prefix=prefix)
app.include_router(designation.router, prefix=prefix)
app.include_router(awards.router, prefix=prefix)
app.include_router(research.router, prefix=prefix)
app.include_router(publication.router, prefix=prefix)
app.include_router(funding.router, prefix=prefix)
# app.include_router(image.router, prefix=prefix)
# app.include_router(cv.router, prefix=prefix)
