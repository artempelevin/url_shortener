import uvicorn
from fastapi import FastAPI

from app.config import config
from app.routers import urls


def create_app() -> FastAPI:
    _app = FastAPI(
        title='Url Shortener',
        version='0.1.1'
    )
    _app.include_router(router=urls.router, prefix='/api/v1/urls', tags=['urls'])
    return _app


app = create_app()

if __name__ == '__main__':
    uvicorn.run(
        app="app.main:app",
        host=config.server.host,
        port=config.server.port,
        reload=config.deploy.debug
    )
