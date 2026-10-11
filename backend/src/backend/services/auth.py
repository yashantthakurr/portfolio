
from backend.auth import security
from backend.exceptions.auth import INVALID_CREDENTIALS_EXCEPTION
from backend.models.users import User
from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from typing import Dict

def login(db: Session, data: OAuth2PasswordRequestForm) -> Dict[str, str]:
    user = db.query(User).filter(User.username==data.username).first()
    if not user or not security.verify_password(data.password, user.hashed_password):
        raise INVALID_CREDENTIALS_EXCEPTION
    return {
        "access_token": security.get_access_token(data.username),
        "token_type": "bearer"
    }
