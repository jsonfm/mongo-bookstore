from typing import List, Literal, Optional, Union

from pydantic import BaseModel

from app.schemas.base import CustomBaseModel

Genres = (
    Literal["science"]
    | Literal["classic"]
    | Literal["philosophy"]
    | Literal["literature"]
    | Literal["novel"]
    | Literal["romance"]
    | Literal["mistery"]
    | Literal["suspense"]
    | Literal["terror"]
    | Literal["economics"]
    | Literal["business"]
    | Literal["history"]
    | Literal["non-fiction"]
    | Literal["fantasy"]
    | Literal["policy"]
    | Literal["arts and humanities"]
    | Literal["journalism"]
)


GenresType = List[Genres]
BookWeightUnits = Literal["gr"]


class BookWeight(BaseModel):
    value: float
    units: BookWeightUnits


BookDimensionsUnits = Literal["cm"]


class BookDimensions(BaseModel):
    width: float
    height: float
    large: float
    units: BookDimensionsUnits


class BookImage(BaseModel):
    url: str
    metadata: dict


class Book(CustomBaseModel):
    name: str
    description: str
    edition_year: int
    pages_number: int
    authors: list
    editorial: str
    genres: Optional[GenresType] = []
    isbn: Optional[str] = None
    dimensions: Optional[BookDimensions] = None
    weight: Optional[BookWeight] = None
    images: Optional[List[BookImage]] = []
