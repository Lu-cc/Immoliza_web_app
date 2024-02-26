# Import modules
from fastapi import FastAPI
from typing import Union

app = FastAPI()


@app.get("/")
def health():
    return {"message": "Server is Running"}

print('this is an update inside dev')