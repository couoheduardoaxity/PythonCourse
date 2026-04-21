from app.model import save_model, train_model
from app.preprocessing import clean_data, load_data


def main():
    df = load_data("data/dataset.csv")
    df = clean_data(df)

    model = train_model(df)
    save_model(model)

    print("✅ Modelo entrenado y guardado en models/model.joblib")


if __name__ == "__main__":
    main()
