from typing import Any, List

from fastapi import APIRouter

from app import schemas
from app.models import Joke

router = APIRouter()


@router.get("", response_model=List[schemas.JokeResponse])
def read_jokes() -> Any:
    """
    Retrieve a single joke
    """

    joke = Joke().get_new_joke()

    return [joke]
