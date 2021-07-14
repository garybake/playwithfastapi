from typing import Any, List

from fastapi import APIRouter
from fastapi.responses import HTMLResponse


from app import schemas
from app.models import Joke
from app.main import templates
# import app

router = APIRouter()


@router.get("", response_model=List[schemas.JokeResponse])
def read_jokes() -> Any:
    """
    Retrieve a single joke
    """

    joke = Joke().get_new_joke()

    return [joke]

#
@router.get("/page", response_class=HTMLResponse)
def render_page() -> Any:
    return app.templates.TemplateResponse("page.html")
