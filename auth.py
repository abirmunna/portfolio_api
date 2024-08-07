from fastapi_login import LoginManager
from fastapi_login.exceptions import InvalidCredentialsException

from business_logic import models, schemas
from database import SessionLocal


manager = LoginManager("secret", "/login")

@manager.user_loader()
def get_user(email: str):
    db = SessionLocal()
    user_data = db.query(models.User).filter(models.User.email == email).first()
    res = schemas.user(**user_data.__dict__)
    return res