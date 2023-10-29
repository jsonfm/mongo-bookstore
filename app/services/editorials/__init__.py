from app.db import db
from app.services.base import BaseService


class EditorialsService(BaseService):
    """Editorials service"""


#
collection = db["editorials"]
editorialsService = EditorialsService(collection=collection)
