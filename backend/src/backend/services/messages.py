
from backend.models.messages import Message
from backend.schemas.messages import MessageCreate
from backend.services.mailer import send_emails
from fastapi import BackgroundTasks
from sqlalchemy.orm import Session
from typing import List

def send_message(db: Session, data: MessageCreate, background_tasks: BackgroundTasks) -> Message:

    message = Message(**data.model_dump())
    db.add(message)
    db.commit()
    db.refresh(message)

    background_tasks.add_task(
        send_emails,
        receiver_email=data.email,
        receiver_subject="Message Received!",
        receiver_content="(This is an automated message.)\nHey there!\nI received your message and I'll revert back to you shortly.",
        admin_subject=f"{data.name} messaged you via portfolio's contact form",
        admin_content=data.message
    )

    return message

def fetch_all_messages(db: Session) -> List[Message]:
    return db.query(Message).all()
