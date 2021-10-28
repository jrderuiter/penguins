import os
from pathlib import Path

from google.cloud import bigquery

import joblib
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline

    
def train_model(df):
    train = df[["species", "island", "sex"]].dropna().loc[lambda row: row.sex != "."]

    x = train.drop("sex", axis=1)
    y = train["sex"].map({'MALE':0, 'FEMALE':1}).astype(int)

    model = Pipeline(
        steps=[
            (
                "feature_engineering", 
                ColumnTransformer(
                  transformers=[("one_hot", OneHotEncoder(), ["species", "island"])],
                  remainder="drop"
                )
            ),
            (
                "model",
                RandomForestClassifier()
            )       
        ]
    )

    model.fit(x, y)

    return model
