# Import modules
from fastapi import FastAPI
from typing import Union

app = FastAPI()


@app.get("/")
def health():
    return {"message": "Server is Running"}


@app.post("/predict")
def prediction_calculator(property_data: Property):
    try:
        prediction = predict(property_data.dict())
        return prediction
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

print('this is an update inside dev')