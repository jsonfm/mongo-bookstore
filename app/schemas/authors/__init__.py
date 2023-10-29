from typing import List, Optional

from pydantic import BaseModel

from app.schemas.base import CustomBaseModel


class AuthorImage(BaseModel):
    url: str
    metadata: dict


class Author(CustomBaseModel):
    name: str
    bio: str
    images: Optional[List[AuthorImage]]
