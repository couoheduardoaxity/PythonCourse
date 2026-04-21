import os

import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


def train_model(df):
    X = df.drop("target", axis=1)
    y = df["target"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    return model


def save_model(model, path="models/model.joblib"):
    os.makedirs("models", exist_ok=True)
    joblib.dump(model, path)


def load_model(path="models/model.joblib"):
    return joblib.load(path)
