
from backend.database.base import Base
from datetime import datetime
from sqlalchemy import DateTime, func, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

class Message(Base):

    __tablename__ = "messages"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
        index=True
    )

    name: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    email: Mapped[str] = mapped_column(
        String(254),
        nullable=False
    )

    message: Mapped[str] = mapped_column(
        String(400),
        nullable=False
    )

    date_received: Mapped[datetime] = mapped_column(
        DateTime(timezone=False),
        nullable=False,
        default=func.now(),
        server_default=func.now()
    )
