from typing import Optional

# pydantic
from pydantic import BaseModel


class CreateBookForm(BaseModel):
    name: str
    description: str


class UpdateBookForm(BaseModel):
    name: Optional[str]
    description: Optional[str]
