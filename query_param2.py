from fastapi import FastAPI
from fastapi import FastAPI, Query
from pydantic import BaseModel, Field
from typing import Annotated, Literal


app=FastAPI()
# these parameters are query parameters
# means that these are url parameters and not the request parameters
# request body parameters are used for the data inside the function

# this is an example of query parameter
@app.get("/items/")
async def get_items(
    limit: int = Query(10, gt=0, le=100, description="Max items to return"),
    offset: int = Query(0, ge=0, description="Skip N items"),
    order_by: str = Query("created_at", description="Sorting field"),
):
    return {"limit": limit, "offset": offset, "order_by": order_by}

#this is an example of request body parameters

class FilterParams(BaseModel):
    limit: int = Field(100, gt=0, le=100)
    offset: int = Field(0, ge=0)
    order_by: Literal["created_at", "updated_at"] = "created_at"
    tags: list[str] = []


@app.get("/it/")
async def read_items(filter_query: Annotated[FilterParams, Query()]):
    return filter_query