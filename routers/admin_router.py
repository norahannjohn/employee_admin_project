"""
Admin router.

Provides admin endpoints for managing asset requests.
"""

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)
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
    try:
        return admin_handler.get_all_requests(
            db=db,
        )

    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to retrieve requests.",
        ) from exc


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
    try:
        return admin_handler.approve_request(
            db=db,
            request_id=request_id,
            comment_data=comment_data,
        )

    except ValueError as exc:
        message = str(exc)

        if message == "Request not found.":
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=message,
            ) from exc

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=message,
        ) from exc

    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to approve request.",
        ) from exc


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
    try:
        return admin_handler.reject_request(
            db=db,
            request_id=request_id,
            comment_data=comment_data,
        )

    except ValueError as exc:
        message = str(exc)

        if message == "Request not found.":
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=message,
            ) from exc

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=message,
        ) from exc

    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to reject request.",
        ) from exc
