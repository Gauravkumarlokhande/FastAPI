from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union

app = FastAPI()

# we can decide the response type from a function 
class Item(BaseModel):
    name: str
    description: Union [str , None] = None
    price: float
    tax: Union [float , None] = None
    tags: list[str] = []


@app.get("/items/",status_code=201)
async def create_item(item: Item) ->  list[Item]:
    return item


