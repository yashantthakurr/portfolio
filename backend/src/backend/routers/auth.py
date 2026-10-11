
from backend.constants.naming import AUTH_API_PREFIX
from backend.dependencies.database import get_db
from backend.dependencies.rate_limiting import limiter
from backend.services import auth as auth_service
from fastapi import APIRouter, Depends, Request
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from typing import Annotated, Dict

router = APIRouter(
    prefix=AUTH_API_PREFIX,
    tags=["Auth Routes"]
)

@limiter.limit("5/minute")
@router.post("/login", response_model=None)
async def login(db: Annotated[Session, Depends(get_db)], request: Request, data: OAuth2PasswordRequestForm = Depends()):
    return auth_service.login(db, data)
