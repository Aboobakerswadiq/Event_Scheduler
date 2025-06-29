import pytest
from app import app
import json


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_create_event(client):
    res = client.post('/events', json={
        "title": "Test Event",
        "description": "Pytest check",
        "start_time": "2025-06-30T10:00:00",
        "end_time": "2025-06-30T11:00:00"
    })
    assert res.status_code == 201
    data = res.get_json()
    assert data['title'] == "Test Event"
    assert "id" in data


def test_get_events(client):
    res = client.get('/events')
    assert res.status_code == 200
    data = res.get_json()
    assert isinstance(data, list)


def test_search_event(client):
    res = client.get('/events/search?q=Test')
    assert res.status_code == 200
