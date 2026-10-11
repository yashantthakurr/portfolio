
from backend.constants.config import secrets
from pwdlib import PasswordHash
from typing import Dict
from datetime import datetime, timedelta, timezone
from jose import jwt

password_hasher = PasswordHash.recommended()

def hash_password(plain_password: str) -> str:
    return password_hasher.hash(plain_password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return password_hasher.verify(plain_password, hashed_password)

def get_access_token(username: str) -> str:
    expire = datetime.now(timezone.utc) + timedelta(minutes=secrets.ACCESS_TOKEN_EXPIRE_MINUTES)
    payload: Dict[str, str | datetime] = {
        "sub": username,
        "exp": expire
    }
    return jwt.encode(payload, secrets.SECRET_KEY, secrets.ALGORITHM)
