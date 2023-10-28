from app.db import db
from app.services.base import BaseService


class BooksService(BaseService):
    """Books service"""


#
collection = db["books"]
booksService = BooksService(collection=collection)
