import uvicorn

from fastapi import FastAPI
# from fastapi.templating import Jinja2Templates

from app.api.v1 import api_router
from app.core import settings

app = FastAPI(title=settings.PROJECT_NAME)


app.include_router(api_router, prefix=settings.API_V1_STR)

if __name__ == "__main__":
    uvicorn.run('app.main:app', host="0.0.0.0", port=8000, reload=True)


