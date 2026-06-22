"""
Asset request model.

Defines the asset_requests table for storing employee asset requests.
"""

from datetime import datetime
from enum import Enum

from sqlalchemy import DateTime, Enum as SqlEnum, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.db import Base


class RequestStatus(str, Enum):
    """
    Enum representing asset request status.
    """

    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"
    CANCELLED = "cancelled"


class AssetRequest(Base):
    """
    SQLAlchemy model representing an employee asset request.
    """

    __tablename__ = "asset_requests"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
    )

    asset_type_id: Mapped[int] = mapped_column(
        ForeignKey("asset_types.id"),
    )

    reason: Mapped[str] = mapped_column(
        Text,
    )

    status: Mapped[RequestStatus] = mapped_column(
        SqlEnum(RequestStatus),
        default=RequestStatus.PENDING,
    )

    admin_comment: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now,
        onupdate=datetime.now,
    )

    user: Mapped["User"] = relationship(
        back_populates="requests",
    )

    asset_type: Mapped["AssetType"] = relationship(
        back_populates="requests",
    )
