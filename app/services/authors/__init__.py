from app.db import db
from app.services.base import BaseService


class AuthorsService(BaseService):
    """Authors service"""


#
collection = db["authors"]
authorsService = AuthorsService(collection=collection)
