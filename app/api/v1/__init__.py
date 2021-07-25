from fastapi import APIRouter

from app.api.v1 import jokes, locations

api_router = APIRouter()
api_router.include_router(jokes.router, prefix="/jokes", tags=["jokes"])
api_router.include_router(
    locations.router, prefix="/locations", tags=["locations"]
)
