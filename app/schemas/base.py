import uuid

from pydantic import BaseModel, Field
from pydantic_mongo import ObjectIdField


class CustomBaseModel(BaseModel):
    # _id = str = Field(default_factory=uuid.uuid4, alias="_id")
    # id: ObjectIdField
    created_at: str
    updated_at: str
    deleted: bool
    hidden: bool
