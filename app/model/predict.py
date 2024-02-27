import click
import joblib
import pandas as pd


@click.command()
@click.option(
    "-a", "--living-area", type=float, help="Living area of the house", required=True
)
@click.option(
    "-e",
    "--energy-consumption",
    type=float,
    help="Energy consumption of the house",
    required=True,
)
@click.option(
    "-m",
    "--model-path",
    default="artifacts.joblib",
    help="Path to the trained model",
    required=True,
)
def predict(living_area, energy_consumption, model_path):
    """Predicts house prices from 'input_dataset', stores it to 'output_dataset'."""
    ### -------- DO NOT TOUCH THE FOLLOWING LINES -------- ###
    # Load the data
    data = pd.DataFrame(
        {"living_area": [living_area], "energy_consumption": [energy_consumption]}
    )
    ### -------------------------------------------------- ###

    # Load the model artifacts using joblib
    artifacts = joblib.load("artifacts.joblib")

    # Unpack the artifacts
    num_features = artifacts["features"]["num_features"]
    # fl_features = artifacts["features"]["fl_features"]
    # cat_features = artifacts["features"]["cat_features"]
    imputer = artifacts["imputer"]
    # enc = artifacts["enc"]
    model = artifacts["model"]
    scaler = artifacts["scaler"]

    # Extract the used data
    data = data[num_features]

    # Apply imputer and encoder on data
    data[num_features] = scaler.transform(data[num_features])
    data[num_features] = imputer.transform(data[num_features])
    # data_cat = enc.transform(data[cat_features]).toarray()

    # Combine the numerical and one-hot encoded categorical columns
    # data = pd.concat(
    #     [
    #         data[num_features + fl_features].reset_index(drop=True),
    #         pd.DataFrame(data_cat, columns=enc.get_feature_names_out()),
    #     ],
    #     axis=1,
    # )

    # Make predictions
    predictions = model.predict(data)
    predictions = predictions  # just picking 10 to display sample output :-)

    ### -------- DO NOT TOUCH THE FOLLOWING LINES -------- ###
    # Save the predictions to a CSV file (in order of data input!)
    # pd.DataFrame({"predictions": predictions}).to_csv(output_dataset, index=False)
    click.echo(f"Predicted house price: {predictions[0]}")
    # Print success messages
    click.echo(click.style("Predictions generated successfully!", fg="green"))
    click.echo(
        f"Nbr. observations: {data.shape[0]} | Nbr. predictions: {predictions.shape[0]}"
    )
    ### -------------------------------------------------- ###


if __name__ == "__main__":
    # how to run on command line:
    # python .\predict.py -i "data\input.csv" -o "output\predictions.csv"
    predict()
