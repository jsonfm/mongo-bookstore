from fastapi import APIRouter

# response
from app.schemas.books.responses import GetBooksResponse

# services
from app.services.books import booksService

router = APIRouter(prefix="/books", tags=["Books"])


@router.get("/")
def get_books(limit: int = 30, offset: int = 0):
    books = booksService.get_books(limit, offset)
    print(books)
    return []


@router.get("/{book_id}")
def get_book(book_id: str):
    return {}


@router.post("/")
def create_book():
    return {}


@router.put("/{book_id}")
def update_book(book_id: str):
    return {}


@router.delete("/{book_id}")
def delete_book(book_id: str):
    return {}


@router.delete("/{book_id}/permanently")
def delete_book_permanently(book_id: str):
    return {}
