from fastapi import APIRouter, Query, Path, Body
from typing import Union, Annotated
from _models.item import Item, OmitItem
from _models.user import User

router = APIRouter()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

# Declare data model as a parameter
@router.post("/items/", response_model=Item, status_code=201)
async def create_item(item: Item):
    return item
    # item_dict = item.dict()
    # if item.tax:
    #     price_with_tax = item.price + item.tax
    #     item_dict.update({"price_with_tax": price_with_tax})
    # return item_dict

# Multiple body parameters
@router.put("/items/{item_id}")
async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)], user: User):
    results = {"item_id":item_id, "item": item, "user": user}
    return results

# Request body + path + query parameters
# @router.put("/items/{item_id}")
# async def update_item(item_id: str, item: Item, q:Union[str, None] = None):

# Mix Path, Query and body parameters
# @router.put("/items/{item_id}")
# async def update_item(
#     item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
#     q: Union[str, None] = None,
#     item: Union[Item, None] = None,
# ):
    # result = {"item_id":item_id, **item.dict()}
    # if q:
    #     result.update({"q": q})
    # return result 

@router.get("/items/")
# async def read_items(q: Annotated[Union[str, None], Query(min_length=3, max_length=50, regex="^fixedquery$")] = None):
# async def read_items(q: Annotated[str, Query(min_length=3)] = "fixedquery"):
async def read_items(q: str):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# Path parameters
@router.get("/items/{item_id}")
async def read_item(item_id: str, q:Union[str, None] = None, short:bool = False):
    item = {"item_id": item_id} 
    if q:
        item.update({"q": q})
    if not short:
        item.update({"description": "This is an amazing item that has a long description"})
    return item

# Path parameters and numeric validations
# @router.get("/items/{item_id}")
# async def read_items(
#     item_id: Annotated[int, Path(title="The ID of the item to get")],
#     q: Annotated[Union[str, None], Query(alias="item-query")] = None,
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results

testItems= {
    "foo": {"name": "Foo"},
    "bar": {"name": "Bar", "description": "The bartenders", "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "tax": 10.5},
}

# response_model_exclude_unset => default values won't be included in the response
@router.get("/items/test/{item_id}", response_model=OmitItem, response_model_exclude_unset=True)
async def read_item(item_id: str):
    return testItems[item_id]