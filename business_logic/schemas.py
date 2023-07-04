from pydantic import BaseModel
from typing import Union, Optional


class user(BaseModel):
    email: str
    pwd: str


class about(BaseModel):
    id: int
    name: Optional[str]
    motto: Optional[str]
    bio: Optional[str]


class create_designation(BaseModel):
    name: Optional[str]
    company: Optional[str]
    location: Optional[str]


class designation(create_designation):
    id: int


class create_awards(BaseModel):
    title: Optional[str]
    year: Optional[str]


class awards(create_awards):
    id: int


class create_funding(BaseModel):
    year: Optional[str]
    title: Optional[str]
    role: Optional[str]
    awarded_amount: Optional[str]
    time_period: Optional[str]
    doner: Optional[str]


class funding(create_funding):
    id: int


class create_publications(BaseModel):
    title: Optional[str]
    published: Optional[str]
    authors: Optional[str]
    research_id: int


class publications(create_publications):
    id: int

    class Config:
        orm_mode = True


class create_research(BaseModel):
    title: str
    description: str


class research(create_research):
    id: int
    publications: Optional[list[publications]]

    class Config:
        orm_mode = True
