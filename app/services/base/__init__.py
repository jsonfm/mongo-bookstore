from bson import ObjectId
from pymongo.collection import Collection

from app.db import db
from app.utils.bson import to_dict
from app.utils.timestamps import add_create_timestamp, add_update_timestamp


class BaseService:
    """Base service with common CRUD operations."""

    def __init__(self, collection: Collection):
        self.collection = collection

    @to_dict
    def get_items(self, limit: int = 30, offset: int = 0):
        items = list(self.collection.find(limit=limit, skip=offset))
        return items

    @to_dict
    def get_item(self, item_id: str):
        item = self.collection.find_one({"_id": ObjectId(item_id)})
        return item

    @to_dict
    def create(self, data: dict):
        add_create_timestamp(data)
        result = self.collection.insert_one(data)
        if not result.acknowledged:
            raise Exception("Object couldn't be created")
        item = self.get_item(result.inserted_id)
        return item

    @to_dict
    def update(self, item_id: str, data: dict):
        add_update_timestamp(data)
        result = self.collection.update_one({"_id": ObjectId(item_id)}, {"$set": data})
        if result.modified_count != 1:
            raise Exception(f"item `f{item_id}` was not updated.")
        item = self.get_item(item_id)
        return item

    @to_dict
    def delete_permanently(self, item_id: str):
        result = self.collection.delete_one({"_id": ObjectId(item_id)})
        if result.deleted_count < 1:
            item_id = None
        return {"item_id": item_id}
