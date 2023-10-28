from fastapi import FastAPI

# routers
from app.api import router


def get_app() -> FastAPI:
    app = FastAPI(title="Bookstore", description="A bookstore backend app with Mongo 💚")
    app.include_router(router)
    return app
