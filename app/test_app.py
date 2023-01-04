"""
    FITEC STUDENT FINAL PROJECT
    UNIT TEST
    BY : Abdel, Julien, Mehdi
"""
from app import app

def test_health_route():
    """
    Healthcheck method at /health to allow kubernetes healthcheck
    """
    response = app.test_client().get('/health')

    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'ok'

def test_hello_route():
    """
    Hello method at / API endpoint to greet user and return number of visit
    """
    response = app.test_client().get('/')
 
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Hello'
