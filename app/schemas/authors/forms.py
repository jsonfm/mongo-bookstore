from pydantic import BaseModel

# schemas
from app.schemas.authors import Author


class CreateAuthorForm(BaseModel):
    name: str
    bio: str
