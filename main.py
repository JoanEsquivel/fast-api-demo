from enum import Enum
from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import Annotated

app = FastAPI(title="Fast API demo for JoanMedia",   description="This is a custom description for my demo API.", version="1.0.0")

# ----------------- Path Parameters -----------------
@app.get("/users/me", tags=["Users"], summary="Get the current user")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}", tags=["Users"], summary="Get a specific user")
async def read_user(user_id: str):
    return {"user_id": user_id}



#Models with fixed data

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get("/models/{model_name}", tags=["Models"], summary="Get a specific LLM model")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

# ----------------- Query Parameters -----------------

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/", tags=["Items"], summary="Get all items")
async def read_item(skip: int = 0, limit: int = 10):
    # Slicing is a way to extract a portion of a list, tuple, string, or any other sequence type. 
    # sequence[start:stop:step]
    # start: The index where the slice starts (inclusive).
    # stop: The index where the slice ends (exclusive).
    # step: The interval between each index (optional).
    return fake_items_db[skip : skip + limit]

@app.get("/items/{item_id}", tags=["Items"], summary="Get a specific item")
async def read_item(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

@app.get("/users/{user_id}/items/{item_id}", tags=["Items"], summary="Get a specific item for a user")
async def read_user_item(
    user_id: int, item_id: str, q: str | None = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

# ----------------- Request Body -----------------
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

@app.post("/items/", tags=["Items"], summary="Create an item")
async def create_item(item: Item):
    return item

@app.put("/items/{item_id}", tags=["Items"], summary="Update an item")
async def update_item(item_id: int, item: Item, q: Annotated[str | None, Query(title="Test", description="Query string for the items to search in the database that have a good match", min_length=3,max_length=50,pattern="^fixedquery$",
            deprecated=True,)] = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result

# Continue with: https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/