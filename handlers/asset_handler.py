from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from models.asset_type import AssetType
from schema.asset_schema import CreateAssetTypeRequest
from schema.asset_schema import UpdateAssetTypeRequest
from services import asset_service


def create_asset(
    db: Session,
    asset_data: CreateAssetTypeRequest,
) -> AssetType:
    """
    Create a new asset type.

    Args:
        db: SQLAlchemy database session.
        asset_data: Asset type details provided by the user.

    Returns:
        AssetType: Newly created asset type.

    Raises:
        HTTPException: If an asset type with the same name already exists.
    """
    try:
        existing_asset = asset_service.get_asset_by_name(
            db=db,
            name=asset_data.name,
        )

        if existing_asset:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Asset type already exists.",
            )

        asset = AssetType(
            name=asset_data.name,
            description=asset_data.description,
        )

        return asset_service.create_asset(
            db=db,
            asset=asset,
        )

    except HTTPException:
        raise
    except Exception:
        raise


def get_all_assets(
    db: Session,
):
    """
    Retrieve all asset types.

    Args:
        db: SQLAlchemy database session.

    Returns:
        list[AssetType]: List of all asset types.
    """
    try:
        return asset_service.get_all_assets(
            db=db,
        )
    except Exception:
        raise


def update_asset(
    db: Session,
    asset_id: int,
    asset_data: UpdateAssetTypeRequest,
):
    """
    Update an existing asset type.

    Args:
        db: SQLAlchemy database session.
        asset_id: Unique asset type identifier.
        asset_data: Updated asset type information.

    Returns:
        AssetType: Updated asset type.

    Raises:
        HTTPException: If the asset type does not exist.
    """
    try:
        asset = asset_service.get_asset_by_id(
            db=db,
            asset_id=asset_id,
        )

        if not asset:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Asset type not found.",
            )

        if asset_data.name is not None:
            asset.name = asset_data.name

        if asset_data.description is not None:
            asset.description = asset_data.description

        return asset_service.update_asset(
            db=db,
            asset=asset,
        )

    except HTTPException:
        raise
    except Exception:
        raise


def deactivate_asset(
    db: Session,
    asset_id: int,
):
    """
    Deactivate an existing asset type.

    Args:
        db: SQLAlchemy database session.
        asset_id: Unique asset type identifier.

    Returns:
        AssetType: Deactivated asset type.

    Raises:
        HTTPException: If the asset type does not exist.
    """
    try:
        asset = asset_service.get_asset_by_id(
            db=db,
            asset_id=asset_id,
        )

        if not asset:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Asset type not found.",
            )

        return asset_service.deactivate_asset(
            db=db,
            asset=asset,
        )

    except HTTPException:
        raise
    except Exception:
        raise
