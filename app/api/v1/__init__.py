from fastapi import APIRouter

from app.api.v1 import jokes

api_router = APIRouter()
api_router.include_router(jokes.router, prefix="/jokes", tags=["jokes"])
