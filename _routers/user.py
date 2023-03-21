from fastapi import APIRouter
from typing import Union

router = APIRouter()

# Order matters
@router.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

@router.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

# Multiple path and query parameters
@router.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: Union[str, None] = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item