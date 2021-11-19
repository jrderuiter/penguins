from typing import Optional, Tuple

import pandas as pd


def preprocess(df: pd.DataFrame) -> Tuple[pd.DataFrame, Optional[pd.Series]]:
    """Pre-processes the given dataset in to features + labels."""

    feature_cols = ["culmen_length_mm",	"culmen_depth_mm",	"flipper_length_mm",	"body_mass_g", "species", "island"]
    label_col = "sex"

    if "sex" in df.columns:
        filtered = (
            df[feature_cols + [label_col]].dropna().loc[lambda row: row.sex != "."]
        )
        features = filtered.drop(label_col, axis=1)
        labels = filtered[label_col].map({"MALE": 0, "FEMALE": 1}).astype(int)
    else:
        features = df[feature_cols]
        labels = None

    return features, labels
