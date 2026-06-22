"""
Defines the users table for storing employee and admin information.
"""

from datetime import datetime
from enum import Enum

from sqlalchemy import Boolean, DateTime, Enum as SqlEnum, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.db import Base


class UserRole(str, Enum):
    """
    Enum representing user roles.
    """

    ADMIN = "admin"
    EMPLOYEE = "employee"


class User(Base):
    """
    SQLAlchemy model representing a system user.
    """

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
    )

    name: Mapped[str] = mapped_column(
        String(100),
    )

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        index=True,
    )

    password_hash: Mapped[str] = mapped_column(
        String(255),
    )

    role: Mapped[UserRole] = mapped_column(
        SqlEnum(UserRole),
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now,
    )

    requests: Mapped[list["AssetRequest"]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan",
    )
