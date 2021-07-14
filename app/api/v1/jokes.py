from typing import Any, List

from fastapi import APIRouter

from app import schemas

router = APIRouter()


@router.get("", response_model=List[schemas.JokeResponse])
def read_jokes() -> Any:
    """
    Retrieve all products.
    """

    joke = {
        'id': 3,
        'the_joke': 'I went to buy some camouflage trousers the other day',
        'the_punchline': "but I couldn't find any"
    }

    return [joke]
