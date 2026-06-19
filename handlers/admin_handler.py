"""
Admin handler.

Handles business logic for admin operations.
"""

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from models.asset_request import RequestStatus
from schema.request_schema import AdminCommentRequest
from services import admin_service


def get_all_requests(
    db: Session,
):
    """
    Retrieve all asset requests.

    Args:
        db: SQLAlchemy database session.

    Returns:
        list: Asset requests.
    """
    try:
        return admin_service.get_all_requests(
            db=db,
        )

    except Exception:
        raise


def approve_request(
    db: Session,
    request_id: int,
    comment_data: AdminCommentRequest,
):
    """
    Approve an asset request.

    Args:
        db: SQLAlchemy database session.
        request_id: Asset request identifier.
        comment_data: Admin comment.

    Returns:
        AssetRequest: Updated asset request.

    Raises:
        HTTPException: If request does not exist or is not pending.
    """
    try:
        asset_request = admin_service.get_request_by_id(
            db=db,
            request_id=request_id,
        )

        if not asset_request:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Request not found.",
            )

        if asset_request.status != RequestStatus.PENDING:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Only pending requests can be approved.",
            )

        asset_request.status = RequestStatus.APPROVED
        asset_request.admin_comment = comment_data.admin_comment

        return admin_service.update_request(
            db=db,
            asset_request=asset_request,
        )

    except HTTPException:
        raise

    except Exception:
        raise


def reject_request(
    db: Session,
    request_id: int,
    comment_data: AdminCommentRequest,
):
    """
    Reject an asset request.

    Args:
        db: SQLAlchemy database session.
        request_id: Asset request identifier.
        comment_data: Admin comment.

    Returns:
        AssetRequest: Updated asset request.

    Raises:
        HTTPException: If request does not exist or is not pending.
    """
    try:
        asset_request = admin_service.get_request_by_id(
            db=db,
            request_id=request_id,
        )

        if not asset_request:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Request not found.",
            )

        if asset_request.status != RequestStatus.PENDING:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Only pending requests can be rejected.",
            )

        asset_request.status = RequestStatus.REJECTED
        asset_request.admin_comment = comment_data.admin_comment

        return admin_service.update_request(
            db=db,
            asset_request=asset_request,
        )

    except HTTPException:
        raise

    except Exception:
        raise
