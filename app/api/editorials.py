from fastapi import APIRouter

# forms
from app.schemas.editorials.forms import CreateEditorialForm

router = APIRouter(prefix="/editorials", tags=["Editorials"])


@router.get("/")
def get_editorials():
    return []


@router.get("/{editorial_id}")
def get_editorial(editorial_id: str):
    return {}


@router.post("/")
def create_editorial(form: CreateEditorialForm):
    return {}


@router.put("/{editorial_id}")
def update_router(editorial_id: str):
    return {}


@router.delete("/{editorial_id}")
def delete_editorial(editorial_id: str):
    return {}


@router.get("/{editorial_id}/permanently")
def delete_editorial_permanently(editorial_id: str):
    return {}
