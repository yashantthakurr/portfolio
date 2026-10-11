
from backend.database.base import Base
from datetime import datetime
from sqlalchemy import DateTime, func, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import ARRAY
from typing import List

class Certificate(Base):

    __tablename__ = "certificates"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
        index=True
    )

    name: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False
    )

    issued_by: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    issued_year: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    skills: Mapped[List[str]] = mapped_column(
        ARRAY(String(20)),
        nullable=False
    )

    certificate_link: Mapped[str] = mapped_column(
        String(200),
        nullable=False
    )

    date_added: Mapped[datetime] = mapped_column(
        DateTime(timezone=False),
        server_default=func.now(),
        default=func.now(),
        nullable=False
    )
