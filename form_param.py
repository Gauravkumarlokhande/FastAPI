from typing import Annotated

from fastapi import FastAPI, Form
# if we want to receive a user input instead of predifined json then we can use form 
app = FastAPI()


@app.post("/login/")
async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    return {"username": username}