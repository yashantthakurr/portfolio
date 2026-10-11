
from backend.constants.naming import MESSAGES_API_PREFIX
from backend.dependencies.auth import get_current_user
from backend.dependencies.database import get_db
from backend.dependencies.rate_limiting import limiter
from backend.models.messages import Message
from backend.models.users import User
from backend.schemas.messages import MessageCreate, ResponseMessage
from backend.services import messages as messages_service
from fastapi import APIRouter, Depends, BackgroundTasks, Request
from sqlalchemy.orm import Session
from typing import Annotated, List

router = APIRouter(
    prefix=MESSAGES_API_PREFIX,
    tags=["Messages Routes"]
)

@router.post("/", response_model=ResponseMessage, status_code=201)
@limiter.limit("5/minute")
async def send_message(db: Annotated[Session, Depends(get_db)], data: MessageCreate, background_tasks: BackgroundTasks, request: Request) -> Message:
    return messages_service.send_message(db, data, background_tasks)

@router.get("/", response_model=List[ResponseMessage])
@limiter.limit("5/minute")
async def get_all_messages(db: Annotated[Session, Depends(get_db)], user: Annotated[User, Depends(get_current_user)], request: Request) -> List[Message]:
    return messages_service.fetch_all_messages(db)
