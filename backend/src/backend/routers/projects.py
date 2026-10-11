
from backend.constants.naming import PROJECTS_API_PREFIX
from backend.dependencies.auth import get_current_user
from backend.dependencies.database import get_db
from backend.dependencies.rate_limiting import limiter
from backend.models.projects import Project
from backend.models.users import User
from backend.schemas.projects import ProjectCreate, ResponseProject, ProjectUpdate
from backend.services import projects as projects_service
from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from typing import Annotated, List

router = APIRouter(
    prefix=PROJECTS_API_PREFIX,
    tags=["Projects Routes"]
)

@router.post("/", response_model=ResponseProject, status_code=201)
@limiter.limit("5/minute")
async def add_project(db: Annotated[Session, Depends(get_db)], user: Annotated[User, Depends(get_current_user)], data: ProjectCreate, request: Request) -> Project:
    return projects_service.add_project(db, data)

@router.get("/", response_model=List[ResponseProject])
@limiter.limit("5/minute")
async def get_all_projects(db: Annotated[Session, Depends(get_db)], request: Request) -> List[Project]:
    return projects_service.fetch_all_projects(db)

@router.patch("/{id}", response_model=ResponseProject)
@limiter.limit("5/minute")
async def update_experience(db: Annotated[Session, Depends(get_db)], user: Annotated[User, Depends(get_current_user)], request: Request, id: int, data: ProjectUpdate) -> Project:
    return projects_service.update_experience(db, id, data)

@router.delete("/{id}", response_model=None, status_code=204)
@limiter.limit("5/minute")
async def delete_project(db: Annotated[Session, Depends(get_db)], user: Annotated[User, Depends(get_current_user)], request: Request, id: int) -> None:
    return projects_service.delete_project(db, id)
