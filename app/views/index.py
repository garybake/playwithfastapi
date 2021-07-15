from typing import Any, List

from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi import Request

from app.core import templates

router = APIRouter()


@router.get("", response_class=HTMLResponse)
async def render_index(request: Request) -> Any:
    return templates.TemplateResponse("index.html", {"request": request})
