
from backend.constants.config import secrets
from backend.dependencies.database import get_db
from backend.exceptions.auth import INVALID_OR_EXPIRED_TOKEN_EXCEPTION
from backend.models.users import User
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from typing import Annotated
from sqlalchemy.orm import Session

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")

def get_current_user(db: Annotated[Session, Depends(get_db)], token: str = Depends(oauth2_scheme)) -> User:
    try:
        payload = jwt.decode(token, secrets.SECRET_KEY, algorithms=[secrets.ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise INVALID_OR_EXPIRED_TOKEN_EXCEPTION
    except JWTError:
        raise INVALID_OR_EXPIRED_TOKEN_EXCEPTION
    user = db.query(User).filter(User.username==username).first()
    if not user:
        raise INVALID_OR_EXPIRED_TOKEN_EXCEPTION
    return user
