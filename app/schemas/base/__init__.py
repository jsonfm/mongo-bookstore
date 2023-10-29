import uuid

from pydantic import BaseModel, Field
from pydantic_mongo import ObjectIdField


class CustomBaseModel(BaseModel):
    id: str = Field(..., alias="_id")
    created_at: str
    updated_at: str
    deleted: bool
    hidden: bool
