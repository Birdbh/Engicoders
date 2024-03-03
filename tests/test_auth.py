import pytest
from flask import session

def test_login(client, auth):
    # test that viewing the page renders without template errors
    assert client.get('/auth/login').status_code == 200
    # test that successful login redirects to the index page
    response = auth.login()
    assert response.headers['Location'] == "/"
    # login request set the user_id in the session
    # check that the user is loaded from the session
    with client:
        client.get('/')
        assert session['user_id'] == 1
        assert g.user['username'] == 'test'