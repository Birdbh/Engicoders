import pytest
from flask import template_rendered
from contextlib import contextmanager
from unittest.mock import patch
import sys

sys.path.append("src")

from flaskr import create_app  # Adjust this to your Flask app creation method
from flaskr.home import home

@pytest.fixture
def app():
    app = create_app({'TESTING': True})
    return app

@pytest.fixture
def client(app):
    return app.test_client()

@contextmanager
def captured_templates(app):
    recorded = []

    def record(sender, template, context, **extra):
        recorded.append((template, context))
    template_rendered.connect(record, app)
    try:
        yield recorded
    finally:
        template_rendered.disconnect(record, app)

def test_home_get(client):
    with captured_templates(app) as templates:
        response = client.get('flaskr/home/')
        assert response.status_code == 200
        assert len(templates) == 1
        template, context = templates[0]
        assert template.name == "home.html"


def test_home_post_success(mock_data_gen, client):
    mock_data_gen_instance = mock_data_gen.return_value
    mock_data_gen_instance.get_time_series.return_value = {}

    post_data = {
        'channel_id': '123',
        'time_increment': '10',
        'field_number': '2',
        'start_date': '2021-01-01 00:00:00'
    }
    response = client.post('flaskr/home/', data=post_data, follow_redirects=True)
    assert response.status_code == 200


def test_home_post_error(mock_data_gen, client):
    mock_data_gen_instance = mock_data_gen.return_value
    mock_data_gen_instance.get_time_series.side_effect = Exception("Error fetching data")

    post_data = {
        'channel_id': '123',
        'time_increment': '10',
        'field_number': '2',
        'start_date': '2021-01-01 00:00:00'
    }
    response = client.post('flaskr/home/', data=post_data)
    assert response.status_code == 500
    assert "Error fetching data from ThingSpeak" in response.data.decode()
