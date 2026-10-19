
from backend.type.job_mode import JobMode
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field
from typing import Optional

class CreateExperience(BaseModel):

    organization: str = Field(..., min_length=5, max_length=40, description="Name of the organization in which have worked")
    role: str = Field(...,min_length=5, max_length=50, description="Name of the position or role offered")
    timeline: str = Field(..., min_length=10, max_length=100, description="Time spent in the organization. Example format July 2026 - August 2026")
    description: str = Field(..., min_length=20, max_length=500, description="Description about the role")
    mode: JobMode = Field(..., description="Whether remote, hybrid or onsite")

class UpdateExperience(BaseModel):

    organization: Optional[str] = Field(None, min_length=5, max_length=40, description="Name of the organization in which have worked")
    role: Optional[str] = Field(None, min_length=5, max_length=50, description="Name of the position or role offered")
    timeline: Optional[str] = Field(None, min_length=10, max_length=100, description="Time spent in the organization. Example format July 2026 - August 2026")
    description: Optional[str] = Field(None, min_length=20, max_length=500, description="Description about the role")
    mode: Optional[JobMode] = Field(None, description="Whether remote, hybrid or onsite")

class ResponseExperience(BaseModel):

    id: int
    organization: str
    role: str
    timeline: str
    description: str
    mode: str
    date_added: datetime

    model_config = ConfigDict(from_attributes=True)
