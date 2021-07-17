from typing import Any, List

from fastapi import APIRouter

from app import schemas
from app.models import Joke

router = APIRouter()


@router.get("", response_model=List[schemas.JokeResponse])
async def read_jokes(joke_type) -> Any:
    """
    Retrieve a single joke
    """
    joke = Joke().get_new_joke(joke_type)
    return [joke]
