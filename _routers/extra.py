from fastapi import APIRouter
from enum import Enum

# Create an Enum class
# By inheriting from str the API docs will be able to know that the values must be of type string and will be able to render correctly.
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet ="lenet"
    
router = APIRouter()

# Declare a path parameter
@router.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    
    return {"model_name": model_name, "message": "Have some residuals"}

# Path converter
@router.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}
