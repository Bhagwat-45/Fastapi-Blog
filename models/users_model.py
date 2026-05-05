from __future__ import annotations
from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database.database import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer,primary_key=True,index=True)
    username: Mapped[str] = mapped_column(String(50), unique=True,nullable=False)
    email: Mapped[str] = mapped_column(String[120],unique=True,nullable=True)
    image_file: Mapped[str| None] = mapped_column(
        String(200),
        nullable=True,
        default=None
    )

    posts: Mapped[list["Post"]] = relationship(back_populates="author", cascade="all, delete-orphan")

    
