
from datetime import datetime
from pydantic import BaseModel, ConfigDict, EmailStr, Field

class MessageCreate(BaseModel):

    name: str = Field(..., min_length=2, max_length=50, description="Name of the sender")
    email: EmailStr = Field(..., max_length=254, description="Email of the sender")
    message: str = Field(..., min_length=1, max_length=400, description="Message of the sender")

class ResponseMessage(BaseModel):

    id: int
    name: str
    email: str
    message: str
    date_received: datetime

    model_config = ConfigDict(from_attributes=True)
