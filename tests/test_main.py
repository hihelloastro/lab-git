import pytest
from fastapi.testclient import TestClient
from main import app

# 재사용
@pytest.fixture
def client():
    return TestClient(app)

# 함수 이름이 test_로 시작하면 자동 실행
def test_hello_world(client):
    response = client.get("/hello")

    assert response.status_code == 200
    assert response.status_code != 500
    assert response.json() == {"message": "Hello World!"}

# pytest -v test_main.py 로 실행