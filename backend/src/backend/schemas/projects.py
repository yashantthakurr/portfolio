
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field
from typing import List, Optional

class ProjectCreate(BaseModel):

    title: str = Field(..., min_length=2, max_length=100, description="Title of the project")
    description: str = Field(..., min_length=10, max_length=400, description="Description of the project")
    technologies: List[str] = Field(..., max_length=30, description="Technologies used in the project")
    github: str = Field(..., max_length=100, description="Github repository of the project")
    live_demo: str | None = Field(max_length=100, default=None, description="Live demo of the project")

class ProjectUpdate(BaseModel):

    title: Optional[str] = Field(None, min_length=2, max_length=100, description="Title of the project")
    description: Optional[str] = Field(None, min_length=10, max_length=400, description="Description of the project")
    technologies: Optional[List[str]] = Field(None, max_length=30, description="Technologies used in the project")
    github: Optional[str] = Field(None, max_length=100, description="Github repository of the project")
    live_demo: Optional[str] = Field(None, max_length=100, description="Live demo of the project")

class ResponseProject(BaseModel):

    id: int
    title: str
    description: str
    technologies: List[str]
    github: str
    live_demo: str | None
    date_added: datetime

    model_config = ConfigDict(from_attributes=True)
