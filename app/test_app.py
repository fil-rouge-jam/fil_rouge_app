import pytest
import json
from app import app

def test_health_route():
    response = app.test_client().get('/health')

    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'ok'
