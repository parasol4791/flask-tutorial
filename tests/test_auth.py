import pytest
from flask import g, session
from flaskr.db import get_db


def test_register(client, app):
    # GET request to register view simply works
    assert client.get('/auth/register').status_code == 200

    # POST request to register redirects to login
    response = client.post(
        '/auth/register', data={'username': 'a', 'password': 'a'}
    )
    assert '/auth/login' == response.headers['Location']

    # Making sure registration of the new user 'a' is in database
    with app.app_context():
        assert get_db().execute(
            "select * from user where username = 'a'",
        ).fetchone() is not None


@pytest.mark.parametrize(('username', 'password', 'message'), (
    ('', '', b'Username is required.'),
    ('a', '', b'Password is required.'),
    ('test', 'test', b'already registered'),
))
def test_register_validate_input(client, username, password, message):
    # User registration failure cases - parametrized by inputs and expected message
    response = client.post(
        '/auth/register',
        data={'username': username, 'password': password}
    )
    assert message in response.data


def test_login(client, auth):
    # GET request to login simply works
    assert client.get('/auth/login').status_code == 200
    # POST request to login redirects to the root (blog section)
    response = auth.login()
    assert response.headers['Location'] == '/'

    # with client block allows to access session parameters after a request is complete
    # Session should have user data in it after a login
    with client:
        client.get('/')
        assert session['user_id'] == 1
        assert g.user['username'] == 'test'


@pytest.mark.parametrize(('username', 'password', 'message'), (
    ('a', 'test', b'Incorrect username.'),
    ('test', 'a', b'Incorrect password.'),
))
def test_login_validate_input(auth, username, password, message):
    # Parametrized test of different failure cases while logging in
    response = auth.login(username, password)
    assert message in response.data


def test_logout(client, auth):
    auth.login()
    # Session should not have a user after a logout
    with client:
        auth.logout()
        assert 'user_id' not in session