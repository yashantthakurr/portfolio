
from backend.constants.naming import EXPERIENCES_API_PREFIX
from backend.dependencies.auth import get_current_user
from backend.dependencies.database import get_db
from backend.dependencies.rate_limiting import limiter
from backend.models.experiences import Experience
from backend.models.users import User
from backend.schemas.experiences import CreateExperience, ResponseExperience, UpdateExperience
from backend.services import experiences as experiences_service
from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from typing import Annotated, List

router = APIRouter(
    prefix=EXPERIENCES_API_PREFIX,
    tags=["Experiences Routes"]
)

@router.post("/", response_model=ResponseExperience)
@limiter.limit("5/minute")
async def add_experience(db: Annotated[Session, Depends(get_db)], user: Annotated[User, Depends(get_current_user)], data: CreateExperience, request: Request) -> Experience:
    return experiences_service.add_experience(db, data)

@router.get("/", response_model=List[ResponseExperience])
@limiter.limit("5/minute")
async def get_all_experiences(db: Annotated[Session, Depends(get_db)], request: Request) -> List[Experience]:
    return experiences_service.fetch_all_experiences(db)

@router.patch("/{id}", response_model=ResponseExperience)
@limiter.limit("5/minute")
async def update_experience(db: Annotated[Session, Depends(get_db)], user: Annotated[User, Depends(get_current_user)], request: Request, id: int, data: UpdateExperience) -> Experience:
    return experiences_service.update_experience(db, id, data)

@router.delete("/{id}", response_model=None, status_code=204)
@limiter.limit("5/minute")
async def delete_experience(db: Annotated[Session, Depends(get_db)], user: Annotated[User, Depends(get_current_user)], request: Request, id: int) -> None:
    return experiences_service.delete_experience(db, id)
