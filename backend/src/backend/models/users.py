
from backend.database.base import Base
from datetime import datetime
from sqlalchemy import DateTime, func, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

class User(Base):

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
        index=True
    )

    username: Mapped[str] = mapped_column(
        String(24),
        nullable=False,
        unique=True
    )

    hashed_password: Mapped[str] = mapped_column(
        String(128),
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=False),
        server_default=func.now(),
        default=func.now(),
        nullable=False
    )
