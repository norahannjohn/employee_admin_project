"""
Admin router.

Provides admin endpoints for managing asset requests.
"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.db import get_db
from core.dependencies import get_current_admin
from handlers import admin_handler
from models.user import User
from schema.request_schema import (
    AdminCommentRequest,
    RequestResponse,
)

router = APIRouter(
    prefix="/admin",
    tags=["Admin"],
)


@router.get(
    "/requests",
    response_model=list[RequestResponse],
)
def get_all_requests(
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin),
):
    """
    Retrieve all asset requests.

    Args:
        db: SQLAlchemy database session.
        current_admin: Authenticated admin user.

    Returns:
        list[RequestResponse]: Asset requests.
    """
    return admin_handler.get_all_requests(
        db=db,
    )


@router.patch(
    "/requests/{request_id}/approve",
    response_model=RequestResponse,
)
def approve_request(
    request_id: int,
    comment_data: AdminCommentRequest,
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin),
):
    """
    Approve an asset request.

    Args:
        request_id: Asset request identifier.
        comment_data: Admin comment.
        db: SQLAlchemy database session.
        current_admin: Authenticated admin user.

    Returns:
        RequestResponse: Updated asset request.
    """
    return admin_handler.approve_request(
        db=db,
        request_id=request_id,
        comment_data=comment_data,
    )


@router.patch(
    "/requests/{request_id}/reject",
    response_model=RequestResponse,
)
def reject_request(
    request_id: int,
    comment_data: AdminCommentRequest,
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin),
):
    """
    Reject an asset request.

    Args:
        request_id: Asset request identifier.
        comment_data: Admin comment.
        db: SQLAlchemy database session.
        current_admin: Authenticated admin user.

    Returns:
        RequestResponse: Updated asset request.
    """
    return admin_handler.reject_request(
        db=db,
        request_id=request_id,
        comment_data=comment_data,
    )
