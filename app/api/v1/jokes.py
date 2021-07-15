from typing import Any, List

from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi import Request


from app import schemas
from app.models import Joke
from app.core import templates

router = APIRouter()


@router.get("", response_model=List[schemas.JokeResponse])
def read_jokes() -> Any:
    """
    Retrieve a single joke
    """

    joke = Joke().get_new_joke()
    return [joke]


@router.get("/page", response_class=HTMLResponse)
def render_page(request: Request) -> Any:
    return templates.TemplateResponse("page.html", {"request": request})
