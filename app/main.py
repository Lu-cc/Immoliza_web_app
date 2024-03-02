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
    
class InputData(BaseModel):
    property_type: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    region: Optional[str] = None
    zip_code: int
    locality: Optional[str] = None
    subproperty_type: Optional[str] = None
    total_area_sqm: int
    nbr_bedrooms: int
    primary_energy_consumption_sqm: Optional[int] = None
    construction_year: Optional[int] = None
    fl_garden: bool
    fl_terrace: bool
    fl_swimming_pool: bool
    fl_floodzone: bool

    @classmethod
    def from_dict(cls, input_data):
        return cls(
            property_type=input_data.get('property_type', None),
            latitude=input_data.get('latitude', None) if input_data.get('latitude', 0.0) != 0.0 else None,
            longitude=input_data.get('longitude', None) if input_data.get('longitude', 0.0) != 0.0 else None,
            region=input_data.get('region', None) if input_data.get('region', '') != '' else None,
            zip_code=input_data.get('zip_code', None) if input_data.get('zip_code', '') != '' else None,
            locality=input_data.get('locality', None) if input_data.get('locality', '') != '' else None,
            subproperty_type=input_data.get('subproperty_type', None) if input_data.get('subproperty_type', '') != '' else None,
            total_area_sqm=input_data['total_area_sqm'],
            nbr_bedrooms=input_data['nbr_bedrooms'],
            primary_energy_consumption_sqm=input_data.get('primary_energy_consumption_sqm', None) if input_data.get('primary_energy_consumption_sqm', 0) > 0 else None,
            construction_year=input_data.get('construction_year', None) if input_data.get('construction_year', 0) > 0 else None,
            fl_garden=input_data['fl_garden'],
            fl_terrace=input_data['fl_terrace'],
            fl_swimming_pool=input_data['fl_swimming_pool'],
            fl_floodzone=input_data['fl_floodzone']
        )

@app.get("/")
def health():
    return {"message": "Server is Running"}


@app.post("/predict")
def prediction_calculator(input_data: InputData):
    print(input_data)

    try:
        prediction = predict(input_data.dict())
        return {"predicted_price": prediction}
    except Exception as e:
        print('error in main' + str(e))
        raise HTTPException(status_code=500, detail=str(e))
    

if __name__ == "__main__":
    pass
    #For testing purposes
#     dummy = {"property_type": "HOUSE",
#   "latitude": 0,
#   "longitude": 0,
#   "region": "Flanders",
#   "zip_code": 0,
#   "locality": "Roeselare",
#   "subproperty_type": "MIXED_USE_BUILDING",
#   "total_area_sqm": 0,
#   "nbr_bedrooms": 0,
#   "primary_energy_consumption_sqm": 0,
#   "construction_year": 0,
#   "fl_garden": True,
#   "fl_terrace": True,
#   "fl_swimming_pool": True,
#   "fl_floodzone": True}

#     prediction = prediction_calculator(dummy)
#     print("Predicted house price:", prediction)


# print("this is an update inside ss dev")
