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
                    transformers=[
                        ("categorical", OneHotEncoder(), ["species", "island"]),
                        ("numeric", "passthrough", ["culmen_length_mm",	"culmen_depth_mm",	"flipper_length_mm",	"body_mass_g"])],
                    remainder="drop",
                ),
            ),
            ("model", RandomForestClassifier()),
        ]
    )

    model.fit(features, labels)

    return model
