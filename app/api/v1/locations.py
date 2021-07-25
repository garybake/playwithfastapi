from typing import Any

from fastapi import APIRouter

from app import schemas
from app.models import LocationKey

router = APIRouter()


@router.get("/key", response_model=schemas.LocationKeyResponse)
async def read_locations_key() -> Any:
    """
    Retrieve the locations api key
    """
    key = LocationKey().get_location_key()
    return key
