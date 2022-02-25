import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.library.fibonacci import fibonacci


client = TestClient(app)


def test_home():
    response = client.get(
        "/", headers={"content-type": "text/html; charset=utf-8"})
    assert response.status_code == 200
    assert b"Welcome to FastAPI Website Starter Demo" in response.content
    response = client.get("/static/css/style3.css")
    assert response.status_code == 200


def test_two_forms():
    response = client.get("/twoforms",
                          headers={"content-type": "text/html; charset=utf-8"})
    assert response.status_code == 200
    assert b"Fibonacci number" in response.content


data = [
    (fibonacci(0), 0),
    (fibonacci(1), 1),
    (fibonacci(2), 1),
    (fibonacci(10), 55),
    (fibonacci(14), 377),
    (fibonacci(50), 12586269025),
]

@pytest.mark.parametrize("test_data", data)
def test(test_data):
    assert test_data[0] == test_data[1]

