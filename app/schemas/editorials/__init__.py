from app.schemas.base import CustomBaseModel


class Editorial(CustomBaseModel):
    name: str
    bio: str
