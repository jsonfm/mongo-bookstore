from typing import Optional

# pydantic
from pydantic import BaseModel


class CreateBookForm(BaseModel):
    name: str
    description: str
    year: int
    editorial: str
    authors: Optional[list[str]]


class UpdateBookForm(BaseModel):
    name: Optional[str]
    description: Optional[str]
    year: Optional[int]
    editorial: Optional[str]
    authors: Optional[list[str]]
