import pytest
from flaskr import create_app

@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    # create a temporary data file to isolate the database for each test
    # create the app with common test config
    app = create_app()
    yield app

@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()

def test_home_status_code(client):
    """Start with a blank database."""

    response = client.get('/home')
    assert response.status_code == 200
