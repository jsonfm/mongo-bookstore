from pydantic import BaseModel


class Editorial(BaseModel):
    name: str
    bio: str
