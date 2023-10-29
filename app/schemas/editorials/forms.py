from typing import Optional

from pydantic import BaseModel


class CreateEditorialForm(BaseModel):
    name: str
    description: str


class UpdateEditorialForm(BaseModel):
    name: Optional[str]
    description: Optional[str]
