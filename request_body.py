from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union
# when we need to send data from client side to our API then we need to send it through the request body
# A request body is the data sent by the client to our API and the response body is the data sent by our API to the client
# API always has to send the response body but client need not to be send the request to our API

# the basemodel acts as a verifier for our request bdoy data
class Item(BaseModel):
    name:  Union[str, None] = None
    message :  Union[str, None] = None

app=FastAPI()

@app.post('/items/')
async def greet_item(item:Item):
    return item.dict()