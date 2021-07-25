from app.core.config import settings  # noqa: F401
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
