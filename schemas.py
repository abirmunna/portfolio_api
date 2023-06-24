from pydantic import BaseModel

class about(BaseModel):
    id: int
    name: str 
    motto: str
    bio: str

class create_designation(BaseModel):
    name: str
    company: str
    location: str

class designation(create_designation):
    id: int

class create_awards(BaseModel):
    title: str
    year: str

class awards(create_awards):
    id: int


class create_funding(BaseModel):
    year: str
    title: str
    role: str
    awarded_amount: str
    time_period: str
    doner: str


class funding(create_funding):
    id: int

