# Import modules
from fastapi import FastAPI
from typing import Union

app = FastAPI()


@app.get("/home")
def predict():
    return {"prediction": "float", "status_code": "int"}


@app.post("/predict")
def predict():
    return {"prediction": "float", "status_code": "int"}


print("hello")
