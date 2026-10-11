
from backend.database.base import Base
from datetime import datetime
from sqlalchemy import DateTime, func, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

class Experience(Base):

    __tablename__ = "experiences"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
        index=True
    )

    organization: Mapped[str] = mapped_column(
        String(40),
        nullable=False
    )

    role: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    timeline: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    description: Mapped[str] = mapped_column(
        String(400),
        nullable=False
    )

    mode: Mapped[str] = mapped_column(
        String(7),
        nullable=False
    )

    date_added: Mapped[datetime] = mapped_column(
        DateTime(timezone=False),
        nullable=False,
        default=func.now(),
        server_default=func.now()
    )
