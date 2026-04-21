from app.inference import predict


def test_prediction():
    sample = {"feature1": 3, "feature2": 4}

    result = predict(sample)

    assert result in [0, 1]
