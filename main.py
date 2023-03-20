from fastapi import FastAPI
from enum import Enum
from pydantic import BaseModel
from typing import Union

# Create a data model
class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

# Create an Enum class
# By inheriting from str the API docs will be able to know that the values must be of type string and will be able to render correctly.
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet ="lenet"

# Create a FastAPI instance
# Main point of interaction to create all my API
app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

# Define a path operation decorator, path operation function
@app.get("/")
async def root():
    return {"message": "Hello World"} 

# Declare data model as a parameter
@app.post("/items")
async def create_item(item: Item):
    return item

# Path parameters
@app.get("/items/{item_id}")
async def read_item(item_id: str, q:Union[str, None] = None, short:bool = False):
    item = {"item_id": item_id} 
    if q:
        item.update({"q": q})
    if not short:
        item.update({"description": "This is an amazing item that has a long description"})
    return item

# Order matters
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

# Declare a path parameter
@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    
    return {"model_name": model_name, "message": "Have some residuals"}

# Path converter
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}

# Multiple path and query parameters
@app.get("/users/{user_id}/items/{item_id}")
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