"""
Unit tests for main.py
Author: gh-srinivas
"""

import pytest
from app.main import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_homepage(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to Your Flask Demo App!' in response.data

def test_predict(client):
    response = client.post('/predict', json={'value': 3})
    assert response.status_code == 200
    assert response.get_json()['result'] == 6
