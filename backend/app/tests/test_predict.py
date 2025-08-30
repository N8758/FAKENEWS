from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_predict_endpoint():
    payload = {"text": "Breaking news: The stock market is booming today."}
    response = client.post("/api/v1/predict", json=payload)

    assert response.status_code == 200
    data = response.json()
    assert "label" in data
    assert "confidence" in data
    assert isinstance(data["label"], str)
    assert isinstance(data["confidence"], float)
