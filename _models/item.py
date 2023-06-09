from pydantic import BaseModel, Field, HttpUrl
from typing import Union

class Image(BaseModel):
    url: HttpUrl
    name: str

# Create a data model
# Nested model
class Item(BaseModel):
    name: str
    description: Union[str, None] = Field(
        default=None, title="The description of the item", max_length=300
    )
    price: float = Field(gt=0, description="The price must be greater than zero")
    tax: float | None = Field(default=None, example=3.2)
    tags: list[str] = [] 
    #tags: set[str] = set()
    image: Union[list[Image], None] = None
    
# Deeply nested models
class Offer(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    items: list[Item]
    

class OmitItem(BaseModel):
    name: str
    description: str | None = None
    tax: float = 10.5