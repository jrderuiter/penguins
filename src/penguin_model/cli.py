from pathlib import Path

import joblib
import pandas as pd
import typer

from .model import train_model
from .preprocessing import preprocess

app = typer.Typer()


@app.command()
def train(dataset_path: Path, model_path: Path):
    """Train a model instance on the given dataset."""

    # Read data and train model.
    train = pd.read_parquet(dataset_path)
    train_features, train_labels = preprocess(train)
    model = train_model(train_features, train_labels)

    # Save model.
    model_path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, model_path)


if __name__ == "__main__":
    app()
