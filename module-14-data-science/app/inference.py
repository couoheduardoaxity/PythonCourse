import pandas as pd
from app.model import load_model


def predict(input_data: dict):
    model = load_model()

    df = pd.DataFrame([input_data])

    prediction = model.predict(df)[0]

    return prediction
