from pydantic import BaseModel


class Author(BaseModel):
    name: str
    bio: str
