from enum import Enum

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"hello": "world"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


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


items = [
    {"name": "Item 1"}, {"name": "Item 2"}, {"name": "Item 3"}, {"name": "Item 4"}, {"name": "Item 5"},
    {"name": "Item 6"}, {"name": "Item 7"}, {"name": "Item 8"}, {"name": "Item 9"}, {"name": "Item 10"},
    {"name": "Item 11"}, {"name": "Item 12"}, {"name": "Item 13"}, {"name": "Item 14"}, {"name": "Item 15"},
    {"name": "Item 16"}, {"name": "Item 17"}, {"name": "Item 18"}, {"name": "Item 19"}, {"name": "Item 20"},

]


@app.get("/items/")
async def read_items(skip: int = 0, limit: int = 10):
    """
    Query Parameter
    :param skip:
    :param limit:
    :return:
    """
    return items[skip: skip+limit]
