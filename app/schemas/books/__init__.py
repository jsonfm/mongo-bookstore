from app.schemas.base import CustomBaseModel


class Book(CustomBaseModel):
    name: str
    description: str
    # editorial_id: str
    # author_id: str
