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
    def get_items(
        self,
        limit: int = 30,
        offset: int = 0,
        exclude_deleted: bool = True,
        exclude_hidden: bool = True,
    ):
        """Returns a list of items available from the database."""
        filter_ = {}

        if exclude_deleted:
            filter_["deleted"] = False

        if exclude_hidden:
            filter_["hidden"] = False

        items = list(self.collection.find(filter_, limit=limit, skip=offset))
        return items

    @to_dict
    def get_item(self, item_id: str):
        """Searchs an object given its id."""
        item = self.collection.find_one({"_id": ObjectId(item_id)})
        return item

    @to_dict
    def create(self, data: dict):
        """Creates a new object on the database."""
        add_create_timestamp(data)
        data["deleted"] = False
        data["hidden"] = False
        result = self.collection.insert_one(data)
        if not result.acknowledged:
            raise Exception("Object couldn't be created")
        item = self.get_item(result.inserted_id)
        return item

    @to_dict
    def update(self, item_id: str, data: dict):
        """Updates an object from the database."""
        add_update_timestamp(data)
        result = self.collection.update_one({"_id": ObjectId(item_id)}, {"$set": data})
        if result.modified_count != 1:
            raise Exception(f"item `f{item_id}` was not updated.")
        item = self.get_item(item_id)
        return item

    @to_dict
    def delete(self, item_id: str):
        """Sets `deleted` attribute of an object to `true`."""
        data = {"deleted": True}
        self.update(item_id, data)
        result = {"item_id": item_id}
        return result

    @to_dict
    def restore(self, item_id: str):
        """Restores a `deleted` item."""
        data = {"deleted": False}
        item = self.update(item_id, data)
        return item

    @to_dict
    def delete_permanently(self, item_id: str):
        """Deletes permanently an object from the database."""
        result = self.collection.delete_one({"_id": ObjectId(item_id)})
        if result.deleted_count < 1:
            item_id = None
        return {"item_id": item_id}
