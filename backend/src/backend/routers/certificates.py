
from backend.constants.naming import CERTIFICATES_API_PREFIX
from backend.dependencies.auth import get_current_user
from backend.dependencies.database import get_db
from backend.dependencies.rate_limiting import limiter
from backend.models.certifications import Certificate
from backend.models.users import User
from backend.schemas.certificate import CertificateCreate, CertificateResponse, CertificateUpdate
from backend.services import certificates as certificate_service
from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from typing import Annotated, List

router = APIRouter(
    prefix=CERTIFICATES_API_PREFIX,
    tags=["Certificates Routes"]
)

@router.post("/", response_model=CertificateResponse)
@limiter.limit("5/minute")
async def add_certificate(db: Annotated[Session, Depends(get_db)], user: Annotated[User, Depends(get_current_user)], data: CertificateCreate, request: Request) -> Certificate:
    return certificate_service.add_certificate(db, data)

@router.get("/", response_model=List[CertificateResponse])
@limiter.limit("5/minute")
async def get_all_certificates(db: Annotated[Session, Depends(get_db)], request: Request) -> List[Certificate]:
    return certificate_service.fetch_all_certificates(db)

@router.patch("/{id}", response_model=CertificateResponse)
@limiter.limit("5/minute")
async def update_certificate(db: Annotated[Session, Depends(get_db)], user: Annotated[User, Depends(get_current_user)], request: Request, id: int, data: CertificateUpdate) -> Certificate:
    return certificate_service.update_certificate(db, id, data)

@router.delete("/{id}", response_model=None, status_code=204)
@limiter.limit("5/minute")
async def delete_certificate(db: Annotated[Session, Depends(get_db)], user: Annotated[User, Depends(get_current_user)], request: Request, id: int) -> None:
    return certificate_service.delete_certificate(db, id)
