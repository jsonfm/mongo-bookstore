from fastapi import APIRouter

# models
from app.schemas.books import Book, GenresType

# forms
from app.schemas.books.forms import CreateBookForm, UpdateBookForm

# responses
from app.schemas.books.responses import GetBooksResponse

# services
from app.services.books import booksService
from app.services.books.genres import genres

router = APIRouter(prefix="/books", tags=["Books"])


@router.get("/", response_model=list[Book])
def get_books(limit: int = 30, offset: int = 0):
    books = booksService.get_items(limit, offset)
    return books


@router.get("/genres", response_model=GenresType)
def get_genres():
    return genres


@router.get("/{book_id}")
def get_book(book_id: str):
    book = booksService.get_item(book_id)
    return book


@router.post("/")
def create_book(form: CreateBookForm):
    book = booksService.create(form.dict(), parse_id_keys=["editorial"])
    return book


@router.put("/{book_id}")
def update_book(book_id: str, form: UpdateBookForm):
    book = booksService.update(book_id, form.dict())
    return book


@router.delete("/{book_id}")
def delete_book(book_id: str):
    result = booksService.delete(book_id)
    return result


@router.delete("/{book_id}/permanently")
def delete_book_permanently(book_id: str):
    result = booksService.delete_permanently(book_id)
    return result


@router.post("/{book_id}/restore")
def restore_deleted_book(book_id: str):
    result = booksService.restore(book_id)
    return result
