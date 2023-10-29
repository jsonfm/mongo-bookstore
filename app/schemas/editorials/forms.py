from typing import Optional

from pydantic import BaseModel


class CreateEditorialForm(BaseModel):
    name: str
    description: str
    avatar: str


class UpdateEditorialForm(BaseModel):
    name: Optional[str]
    description: Optional[str]
    avatar: Optional[str]
