from pydantic import BaseModel


class CustomBaseModel(BaseModel):
    created_at: str
    updated_at: str
    deleted: bool
    hidden: bool
