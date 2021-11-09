import os 
from pathlib import Path

import pandas as pd

import joblib
import typer

from .model import train_model

app = typer.Typer()


@app.command()
def train(dataset_path: Path, model_path: Path):
    # Read data and train model.
    train_df = pd.read_parquet(dataset_path)
    model = train_model(train_df)

    # Save model.
    model_path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, model_path)


if __name__ == "__main__":
    app()
