import json
import joblib
import pandas as pd
import sys
import os

# json_dummy={"total_area_sqm": 2000, "primary_energy_consumption_sqm":34}


def predict(input_data):
    """Predicts house prices from input data."""
    # Load the trained model
    print(os.getcwd())
    # this_directory= os.path.dirname('app/model/predict.py')
    # sys.path.append(os.path.join(this_directory, 'app/model/train.py'))

    artifacts = joblib.load("/code/app/model/artifacts.joblib")
    print(artifacts)
    # Prepare the input data
    data = pd.DataFrame(input_data, index = [0])
    
    num_features = artifacts["features"]["num_features"]
    fl_features = artifacts["features"]["fl_features"]
    cat_features = artifacts["features"]["cat_features"]
    imputer = artifacts["imputer"]
    enc = artifacts["enc"]
    model = artifacts["model"]
    
    for feature in ['property_type', 'subproperty_type']:
        if feature in data.columns:
            data[feature] = data[feature].str.upper()

    data[num_features] = imputer.transform(data[num_features])
    data_cat = enc.transform(data[cat_features]).toarray()
    data = pd.concat(
        [
            data[num_features + fl_features].reset_index(drop=True),
            pd.DataFrame(data_cat, columns=enc.get_feature_names_out()),
        ],
        axis=1,
    )

    # Make predictions
    predictions = model.predict(data)

    return predictions[0]


if __name__ == "__main__":
    #pass
    #For testing purposes
    dummy = {"property_type": "HOUSE",
  "latitude": 0,
  "longitude": 0,
  "region": "Flanders",
  "zip_code": 0,
  "locality": "Roeselare",
  "subproperty_type": "MIXED_USE_BUILDING",
  "total_area_sqm": 0,
  "nbr_bedrooms": 0,
  "primary_energy_consumption_sqm": 0,
  "construction_year": 0,
  "fl_garden": True,
  "fl_terrace": True,
  "fl_swimming_pool": True,
  "fl_floodzone": True}

    prediction = predict(dummy)
    print("Predicted house price:", prediction)
