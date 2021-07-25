from logging.config import dictConfig
import logging

import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

from app.api.v1 import api_router
from app.views import view_router
from app.core import settings

# Setup logging
from app.core.log_conf import log_config

dictConfig(log_config)
logger = logging.getLogger("jokes-logger")

logger.info("Starting Jokes App")

# Setup app
app = FastAPI(title=settings.PROJECT_NAME)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Setup routes
app.include_router(view_router)
app.include_router(api_router, prefix=settings.API_V1_STR)


@app.get("/")
async def root():
    """Not the best way of handling root page but I can't find any other way"""
    response = RedirectResponse(url="/pages")
    return response


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
