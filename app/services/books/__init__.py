from app.db import db

collection = db["books"]


class BooksService:
    def get_books(self, limit: int = 30, offset: int = 0):
        books = collection.find(limit=limit, skip=offset)
        return books


booksService = BooksService()
