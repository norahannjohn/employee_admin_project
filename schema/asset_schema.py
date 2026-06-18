from datetime import datetime

from pydantic import BaseModel


class CreateAssetTypeRequest(BaseModel):
    """
    Request schema for creating an asset type.

    Attributes:
        name: Name of the asset type.
        description: Description of the asset type.
    """

    name: str
    description: str


class UpdateAssetTypeRequest(BaseModel):
    """
    Request schema for updating an asset type.

    Attributes:
        name: Updated asset type name.
        description: Updated asset type description.
    """

    name: str | None = None
    description: str | None = None


class AssetTypeResponse(BaseModel):
    """
    Response schema representing an asset type.

    Attributes:
        id: Unique asset type identifier.
        name: Name of the asset type.
        description: Description of the asset type.
        is_active: Indicates whether the asset type is active.
        created_at: Asset type creation timestamp.
    """

    id: int
    name: str
    description: str
    is_active: bool
    created_at: datetime

    model_config = {"from_attributes": True}
