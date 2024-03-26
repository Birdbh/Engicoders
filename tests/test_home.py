import pytest
from flask import url_for, json
from flaskr import create_app  # Adjust this import based on your project structure

@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    app = create_app({'TESTING': True})
    yield app

@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()

def test_home_page_get(client):
    """Test that the home page is accessible via a GET request."""
    response = client.get('/home')
    assert response.status_code == 200
    assert b"Home Page" in response.data
