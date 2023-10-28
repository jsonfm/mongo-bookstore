from pydantic import BaseModel


class CreateEditorialForm(BaseModel):
    name: str
    bio: str
