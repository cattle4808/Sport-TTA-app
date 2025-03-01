from fastapi import FastAPI
import uvicorn

from core.config import settings
from api import router as api

app = FastAPI(
    title=settings.app.APP_NAME,
    version=settings.app.APP_VERSION,
    description=settings.app.APP_DESCRIPTION,
    debug=settings.app.APP_DEBUG
)

app.include_router(
    router=api,
    prefix=settings.api.PREFIX
)

if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host=settings.run.HOST,
        port=settings.run.PORT,
        reload=settings.run.RELOAD,
    )