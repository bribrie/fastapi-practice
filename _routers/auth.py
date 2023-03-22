from fastapi import APIRouter, Form
from typing import Annotated

router = APIRouter()

@router.post("/login/")
async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    return {"username": username}