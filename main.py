from enum import Enum
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def root():
    return {"hello": "world"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"item_id": item_id})
    if not short:
        item.update({"q": q})
    return item


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


items = [
    {"name": "Item 1"}, {"name": "Item 2"}, {"name": "Item 3"}, {"name": "Item 4"}, {"name": "Item 5"},
    {"name": "Item 6"}, {"name": "Item 7"}, {"name": "Item 8"}, {"name": "Item 9"}, {"name": "Item 10"},
    {"name": "Item 11"}, {"name": "Item 12"}, {"name": "Item 13"}, {"name": "Item 14"}, {"name": "Item 15"},
    {"name": "Item 16"}, {"name": "Item 17"}, {"name": "Item 18"}, {"name": "Item 19"}, {"name": "Item 20"},

]


@app.get("/items/")
async def read_items(skip: int = 0, limit: int = 10):
    return items[skip: skip+limit]


@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(user_id: int, item_id: str, q: Optional[str] = None, short: bool = False):
    item = {"item_id": item_id, "owner_id": user_id}

    if q:
        item.update({"q": q})
    if not short:
        item.update({"description": "This is an amazing item ....."})
    return item




@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict
