from pydantic import BaseModel


class about(BaseModel):
    name: str
    motto: str
    bio: str

class designation(BaseModel):
    name: str
    company: str
    location: str