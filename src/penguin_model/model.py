from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder


def train_model(features, labels):
    """Trains the model on the given features/labels."""

    model = Pipeline(
        steps=[
            (
                "feature_engineering",
                ColumnTransformer(
                    transformers=[("one_hot", OneHotEncoder(), ["species", "island"])],
                    remainder="drop",
                ),
            ),
            ("model", RandomForestClassifier()),
        ]
    )

    model.fit(features, labels)

    return model
