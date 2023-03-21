from pydantic import BaseModel
from typing import Union

class User(BaseModel):
    username: str
    full_name: Union[float, None] = None