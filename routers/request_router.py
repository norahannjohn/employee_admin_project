"""

Defines asset request API endpoints.
"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.db import get_db
from core.dependencies import get_current_user
from handlers import request_handler
from models.user import User
from schema.request_schema import (
    CreateRequest,
    RequestResponse,
)

router = APIRouter(
    prefix="/requests",
    tags=["Asset Requests"],
)


@router.post(
    "",
    response_model=RequestResponse,
)
def create_request(
    request_data: CreateRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> RequestResponse:
    """
    Create a new asset request.

    Args:
        request_data: Asset request details.
        db: SQLAlchemy database session.
        current_user: Authenticated user.

    Returns:
        RequestResponse: Newly created asset request.
    """
    try:
        return request_handler.create_request(
            db=db,
            current_user=current_user,
            request_data=request_data,
        )
    except Exception:
        raise


@router.get(
    "/me",
    response_model=list[RequestResponse],
)
def get_my_requests(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> list[RequestResponse]:
    """
    Retrieve all asset requests created by the authenticated user.

    Args:
        db: SQLAlchemy database session.
        current_user: Authenticated user.

    Returns:
        list[RequestResponse]: List of asset requests created by the user.
    """
    try:
        return request_handler.get_my_requests(
            db=db,
            current_user=current_user,
        )
    except Exception:
        raise


@router.get(
    "/{request_id}",
    response_model=RequestResponse,
)
def get_request(
    request_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> RequestResponse:
    """
    Retrieve an asset request by its ID.

    Args:
        request_id: Unique asset request identifier.
        db: SQLAlchemy database session.
        current_user: Authenticated user.

    Returns:
        RequestResponse: Matching asset request.
    """
    try:
        return request_handler.get_request(
            db=db,
            request_id=request_id,
            current_user=current_user,
        )
    except Exception:
        raise


@router.patch(
    "/{request_id}/cancel",
    response_model=RequestResponse,
)
def cancel_request(
    request_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> RequestResponse:
    """
    Cancel a pending asset request.

    Args:
        request_id: Asset request identifier.
        db: SQLAlchemy database session.
        current_user: Authenticated user.

    Returns:
        RequestResponse: Updated asset request.
    """
    try:
        return request_handler.cancel_request(
            db=db,
            request_id=request_id,
            current_user=current_user,
        )
    except Exception:
        raise
