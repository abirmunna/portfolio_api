from pydantic import BaseModel


class about(BaseModel):
    name: str
    motto: str
    bio: str

class designation(BaseModel):
    id: int
    name: str
    company: str
    location: str

class create_designation(BaseModel):
    name: str
    company: str
    location: str

class awards(BaseModel):
    id: int
    title: str
    year: str

class create_awards(BaseModel):
    title: str
    year: str
    