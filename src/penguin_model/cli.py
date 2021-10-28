import os 
from pathlib import Path

from google.cloud import bigquery
import joblib
import typer


from .model import train_model

app = typer.Typer()


@app.command()
def train(train_dataset: str, output_path: str):
    client = bigquery.Client(project=os.environ["CLOUD_ML_PROJECT_ID"])    
    data = client.query(train_dataset).to_dataframe()

    model = train_model(data)

    with Path(output_path).open("wb") as file_:
        joblib.dump(model, file_)


if __name__ == "__main__":
    app()
