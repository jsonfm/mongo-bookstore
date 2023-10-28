from app.schemas.base import CustomBaseModel


class Author(CustomBaseModel):
    name: str
    bio: str
