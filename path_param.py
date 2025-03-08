from fastapi import FastAPI

app = FastAPI()
# we can pass the function argument/parameters as a path of the app

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}