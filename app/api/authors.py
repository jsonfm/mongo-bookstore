from fastapi import APIRouter

# forms
from app.schemas.authors.forms import CreateAuthorForm, UpdateAuthorForm

# services
from app.services.authors import authorsService

router = APIRouter(prefix="/authors", tags=["Authors"])

@router.get("/")
def get_authors(limit: int, offset: int):
    authors = authorsService.get_items(limit=limit, offset=offset)
    return authors

@router.get("/{author_id}")
def get_author(author_id: str):
    author = authorsService.get_item(author_id)
    return author


@router.post("/")
def create_author(form: CreateAuthorForm):
    author = authorsService.create(form.dict())
    return author


@router.put("/{author_id}")
def update_author(author_id: str, form: UpdateAuthorForm):
    author = authorsService.update(author_id, form.dict())
    return author


@router.delete("/{author_id}")
def delete_author(author_id: str):
    return {}

@router.delete("/{author_id}/permanently")
def delete_author_permanently(author_id: str):
    result = authorsService.delete_permanently(author_id)
    return result
