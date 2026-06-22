from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.db import get_db
from handlers import asset_handler
from schema.asset_schema import (
    AssetTypeResponse,
    CreateAssetTypeRequest,
    UpdateAssetTypeRequest,
)

router = APIRouter(
    prefix="/asset-types",
    tags=["Asset Types"],
)


@router.post(
    "",
    response_model=AssetTypeResponse,
)
def create_asset(
    asset_data: CreateAssetTypeRequest,
    db: Session = Depends(get_db),
):
    """
    Create a new asset type.

    Args:
        asset_data: Asset type details provided in the request body.
        db: SQLAlchemy database session.

    Returns:
        AssetTypeResponse: Newly created asset type.
    """
    return asset_handler.create_asset(
        db=db,
        asset_data=asset_data,
    )


@router.get(
    "",
    response_model=list[AssetTypeResponse],
)
def get_all_assets(
    db: Session = Depends(get_db),
):
    """
    Retrieve all asset types.

    Args:
        db: SQLAlchemy database session.

    Returns:
        list[AssetTypeResponse]: List of all asset types.
    """
    return asset_handler.get_all_assets(
        db=db,
    )


@router.patch(
    "/{asset_id}",
    response_model=AssetTypeResponse,
)
def update_asset(
    asset_id: int,
    asset_data: UpdateAssetTypeRequest,
    db: Session = Depends(get_db),
):
    """
    Update an existing asset type.

    Args:
        asset_id: Unique asset type identifier.
        asset_data: Updated asset type information.
        db: SQLAlchemy database session.

    Returns:
        AssetTypeResponse: Updated asset type.
    """
    return asset_handler.update_asset(
        db=db,
        asset_id=asset_id,
        asset_data=asset_data,
    )


@router.delete(
    "/{asset_id}",
    response_model=AssetTypeResponse,
)
def deactivate_asset(
    asset_id: int,
    db: Session = Depends(get_db),
):
    """
    Deactivate an existing asset type.

    Args:
        asset_id: Unique asset type identifier.
        db: SQLAlchemy database session.

    Returns:
        AssetTypeResponse: Deactivated asset type.
    """
    return asset_handler.deactivate_asset(
        db=db,
        asset_id=asset_id,
    )


# asset
