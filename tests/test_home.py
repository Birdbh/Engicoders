import pytest
from flaskr import create_app  # Adjust this import based on your project structure

@pytest.fixture
def app():
    app = create_app({
        'TESTING': True,
        # Additional configuration for testing as needed
    })
    yield app

def test_app_creation(app):
    """Test that the Flask app is created successfully."""
    assert app is not None
