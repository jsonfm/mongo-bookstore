from fastapi import APIRouter

#
from app.api.books import router as router_books
from app.api.authors import router as router_authors


router = APIRouter(prefix="/api/v1")
router.include_router(router_books)
router.include_router(router_authors)