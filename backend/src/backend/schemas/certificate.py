
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field
from typing import Optional, List

class CertificateCreate(BaseModel):
    name: str = Field(..., max_length=100, min_length=3)
    issued_by: str = Field(..., min_length=3, max_length=50)
    issued_year: int = Field(...,ge=2024)
    skills: List[str] = Field(..., min_length=2, max_length=20)
    certificate_link: str = Field(..., max_length=200)

class CertificateUpdate(BaseModel):
    name: Optional[str] = Field(None, max_length=100, min_length=3)
    issued_by: Optional[str] = Field(None, min_length=3, max_length=50)
    issued_year: Optional[int] = Field(None,ge=2024)
    skills: Optional[List[str]] = Field(None, min_length=3, max_length=20)
    certificate_link: Optional[str] = Field(None, max_length=200)

class CertificateResponse(BaseModel):
    id: int
    name: str
    issued_by: str
    issued_year: int
    skills: List[str]
    certificate_link: str
    date_added: datetime

    model_config = ConfigDict(from_attributes=True)
