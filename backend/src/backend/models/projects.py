
from backend.database.base import Base
from datetime import datetime
from sqlalchemy import DateTime, func, Integer, String
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import Mapped, mapped_column
from typing import List

class Project(Base):

    __tablename__ = "projects"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
        index=True
    )

    title: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    description: Mapped[str] = mapped_column(
        String(400),
        nullable=False
    )

    technologies: Mapped[List[str]] = mapped_column(
        ARRAY(String(30)),
        nullable=False
    )

    github: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    live_demo: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True
    )

    date_added: Mapped[datetime] = mapped_column(
        DateTime(timezone=False),
        server_default=func.now(),
        default=func.now(),
        nullable=False
    )
