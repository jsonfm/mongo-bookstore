from typing import List, Optional

# pydantic
from pydantic import BaseModel

# schemas
from app.schemas.authors import Author, AuthorImage


class CreateAuthorForm(BaseModel):
    name: str
    bio: str
    images: Optional[List[AuthorImage]] = None


class UpdateAuthorForm(BaseModel):
    name: Optional[str]
    bio: Optional[str]
    images: Optional[List[AuthorImage]] = None
