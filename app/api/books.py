from fastapi import APIRouter

# models
from app.schemas.books import Book

# forms
from app.schemas.books.forms import CreateBookForm, UpdateBookForm

# responses
from app.schemas.books.responses import GetBooksResponse

# services
from app.services.books import booksService

router = APIRouter(prefix="/books", tags=["Books"])


@router.get("/")
def get_books(limit: int = 30, offset: int = 0):
    books = booksService.get_items(limit, offset)
    return books


@router.get("/{book_id}")
def get_book(book_id: str):
    book = booksService.get_item(book_id)
    return book


@router.post("/")
def create_book(form: CreateBookForm):
    book = booksService.create(form.dict())
    return book


@router.put("/{book_id}")
def update_book(book_id: str, form: UpdateBookForm):
    book = booksService.update(book_id, form.dict())
    return book


@router.delete("/{book_id}")
def delete_book(book_id: str):
    return {}


@router.delete("/{book_id}/permanently")
def delete_book_permanently(book_id: str):
    result = booksService.delete_permanently(book_id)
    return result
