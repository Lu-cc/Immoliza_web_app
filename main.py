# Import
from enum import Enum
from fastapi import FastAPI, HTTPException
from typing import Optional
from pydantic import BaseModel
from app.model.predict import predict

app = FastAPI()


# input_data = {
#         'nbr_bedrooms': nbr_bedrooms,
#         'total_area_sqm': total_area_sqm,
#         'surface_land_sqm': surface_land_sqm,
#         #'latitude': latitude,
#         #'longitude': longitude,
#         #'construction_year': construction_year,
#         'zip_code': zip_code,
#         'primary_energy_consumption_sqm': primary_energy_consumption_sqm,
#         'fl_garden': fl_garden,
#         'fl_terrace': fl_terrace,
#         'fl_swimming_pool': fl_swimming_pool,
#         'fl_floodzone': fl_floodzone,
#         'property_type': property_type
#         }
class PropertyType(str, Enum):
    house = "House"
    apartment = "Apartment"


class InputData(BaseModel):
    nbr_bedrooms: int
    total_area_sqm: int
    surface_land_sqm: int
    primary_energy_consumption_sqm: int
    zip_code: int
    fl_garden: Optional[bool]
    fl_terrace: Optional[bool]
    fl_swimming_pool: Optional[bool]
    fl_floodzone: Optional[bool]
    property_type: PropertyType


@app.get("/")
def health():
    return {"message": "Server is Running"}


@app.post("/predict")
def prediction_calculator(input_data: InputData):
    try:
        prediction = predict(input_data.dict())
        return {"predicted_price": prediction}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# run : uvicorn --host 0.0.0.0 main:app --reload
print("this is an update inside dev")
