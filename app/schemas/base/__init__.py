import datetime
import uuid

from pydantic import BaseModel, Field
from pydantic_mongo import ObjectIdField


class CustomBaseModel(BaseModel):
    id: str = Field(..., alias="_id")
    created_at: datetime.datetime
    updated_at: datetime.datetime
    deleted: bool
    hidden: bool
