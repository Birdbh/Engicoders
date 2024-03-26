import pytest
from flask import Flask, request
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

def test_with_request_context(app):
    with app.test_request_context('/home?name=FlaskTest'):
        # Accessing request.args within the request context
        assert request.args.get('name') == 'FlaskTest'