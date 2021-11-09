from typing import Optional, Tuple

import pandas as pd


def preprocess(df: pd.DataFrame) -> Tuple[pd.DataFrame, Optional[pd.Series]]:
    """Pre-processes the given dataset in to features + labels."""

    if "sex" in df.columns:
        filtered = (
            df[["species", "island", "sex"]].dropna().loc[lambda row: row.sex != "."]
        )
        features = filtered.drop("sex", axis=1)
        labels = filtered["sex"].map({"MALE": 0, "FEMALE": 1}).astype(int)
    else:
        features = df[["species", "island"]]
        labels = None

    return features, labels
