from typing import Optional

# pydantic
from pydantic import BaseModel

# schemas
from app.schemas.authors import Author


class CreateAuthorForm(BaseModel):
    name: str
    bio: str


class UpdateAuthorForm(BaseModel):
    name: Optional[str]
    bio: Optional[str]
