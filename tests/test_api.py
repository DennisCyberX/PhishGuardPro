from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_analyze_url():
    response = client.post("/analyze", json={"url": "https://example.com"})
    assert response.status_code == 200
    assert response.json()["status"] == "success"
