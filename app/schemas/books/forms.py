from pydantic import BaseModel


class CreateBookForm(BaseModel):
    name: str
    description: str
