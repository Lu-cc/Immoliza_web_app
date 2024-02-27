# Import modules
from fastapi import FastAPI, HTTPException
from typing import Optional
from pydantic import BaseModel
from model.predict import predict

app = FastAPI()


def predict():
    return predict


@app.get("/")
def health():
    return {"message": "Server is Running"}


@app.post("/predict")
def prediction_calculator(living_area:int, energy_consumption:int):
    try:
        prediction = predict(living_area, energy_consumption)
        return prediction
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


print("this is an update inside dev")
