from typing import Annotated, Union

from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union [str , None] = None
    price: float
    tax: Union [ float , None ]= None


@app.put("/items/{item_id}")
async def update_item(
    item_id: int,
    q: Union [str , None] = None,
    item: Union [Item , None] = None,
):
    results = {"item_id": item_id}
    return results