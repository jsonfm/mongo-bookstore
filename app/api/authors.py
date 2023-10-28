from fastapi import APIRouter

# forms
from app.schemas.authors.forms import CreateAuthorForm

router = APIRouter(prefix="/authors", tags=["Authors"])

@router.get("/")
def get_authors(limit: int, offset: int):
    return []

@router.get("/{author_id}")
def get_author(author_id: str):
    return {}

@router.post("/")
def create_author(form: CreateAuthorForm):
    return {}

@router.put("/{author_id}")
def update_author(author_id: str):
    return {}

@router.delete("/{author_id}")
def delete_author(author_id: str):
    return {}

@router.delete("/{author_id}/permanently")
def delete_author_permanently(author_id: str):
    return {}