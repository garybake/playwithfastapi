from logging.config import dictConfig
import logging

import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
# from fastapi.templating import Jinja2Templates

from app.api.v1 import api_router
from app.views import view_router
from app.core import settings

from app.core.log_conf import log_config
dictConfig(log_config)
logger = logging.getLogger('jokes-logger')

logger.info('Starting Jokes App')
app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(view_router)
app.include_router(api_router, prefix=settings.API_V1_STR)


@app.get("/")
async def root():
    """Not the best way of handling root page but I can't find any other way"""
    response = RedirectResponse(url='/pages')
    return response

if __name__ == "__main__":
    uvicorn.run('app.main:app', host="0.0.0.0", port=8000, reload=True)
