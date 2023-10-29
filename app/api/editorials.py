from fastapi import APIRouter

# forms
from app.schemas.editorials.forms import CreateEditorialForm, UpdateEditorialForm

# services
from app.services.editorials import editorialsService

router = APIRouter(prefix="/editorials", tags=["Editorials"])


@router.get("/")
def get_editorials(limit: int = 30, offset: int = 0):
    items = editorialsService.get_items(limit=limit, offset=offset)
    return items


@router.get("/{editorial_id}")
def get_editorial(editorial_id: str):
    item = editorialsService.get_item(editorial_id)
    return item


@router.post("/")
def create_editorial(form: CreateEditorialForm):
    item = editorialsService.create(form.dict())
    return item


@router.put("/{editorial_id}")
def update_router(editorial_id: str, form: UpdateEditorialForm):
    item = editorialsService.update(editorial_id, form.dict())
    return item


@router.delete("/{editorial_id}")
def delete_editorial(editorial_id: str):
    result = editorialsService.delete(editorial_id)
    return result


@router.delete("/{editorial_id}/permanently")
def delete_editorial_permanently(editorial_id: str):
    result = editorialsService.delete_permanently(editorial_id)
    return result
