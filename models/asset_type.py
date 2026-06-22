"""
Asset type model.

Defines the asset_types table for storing available company assets.
"""

from datetime import datetime

from sqlalchemy import Boolean, DateTime, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.db import Base


class AssetType(Base):
    """
    SQLAlchemy model representing an asset type.
    """

    __tablename__ = "asset_types"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
    )

    name: Mapped[str] = mapped_column(
        String(100),
        unique=True,
    )

    description: Mapped[str] = mapped_column(
        Text,
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
        back_populates="asset_type",
    )
