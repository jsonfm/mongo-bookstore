from bson.objectid import ObjectId

from app.db import db
from app.utils.bson import to_dict
from app.utils.timestamps import add_create_timestamp, add_update_timestamp

collection = db["books"]


class BooksService:
    @to_dict
    def get_items(self, limit: int = 30, offset: int = 0):
        books = list(collection.find(limit=limit, skip=offset))
        return books

    @to_dict
    def get_item(self, item_id: str):
        book = collection.find_one({"_id": ObjectId(item_id)})
        return book

    @to_dict
    def create(self, data: dict):
        add_create_timestamp(data)
        result = collection.insert_one(data)
        if not result.acknowledged:
            raise Exception("Object couldn't created")
        book = self.get_item(book.inserted_id)
        return book

    @to_dict
    def update(self, item_id: str, data: dict):
        add_update_timestamp(data)
        result = collection.update_one({"_id": ObjectId(item_id)}, {"$set": data})
        if result.modified_count != 1:
            raise Exception(f"item `f{item_id}` was not updated.")
        book = self.get_item(item_id)
        return book

    @to_dict
    def delete_permanently(self, item_id: str):
        result = collection.delete_one({"_id": ObjectId(item_id)})
        if result.deleted_count < 1:
            item_id = None
        return { "item_id": item_id }


booksService = BooksService()
