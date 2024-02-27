# Import modules
from fastapi import FastAPI, HTTPException
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


def predict():
    return predict


@app.get("/")
def health():
    return {"message": "Server is Running"}


@app.post("/predict")
def prediction_calculator(property_data):
    try:
        prediction = predict(property_data.dict())
        return prediction
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


print("this is an update inside dev")
