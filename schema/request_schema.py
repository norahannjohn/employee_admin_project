"""
Asset request schemas.

Defines request and response models for asset request APIs.
"""

from datetime import datetime

from pydantic import BaseModel

from models.asset_request import RequestStatus


class CreateRequest(BaseModel):
    """
    Schema for creating an asset request.
    """

    asset_type_id: int
    reason: str


class RequestResponse(BaseModel):
    """
    Schema for asset request responses.
    """

    id: int
    asset_type_id: int
    reason: str
    status: RequestStatus
    admin_comment: str | None
    created_at: datetime

    class Config:
        from_attributes = True


class AdminCommentRequest(BaseModel):
    """
    Schema for admin approval/rejection comments.
    """

    admin_comment: str
