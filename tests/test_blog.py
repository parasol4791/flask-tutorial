import pytest
from flaskr.db import get_db


def test_index(client, auth):
    # Before authentication, there suppose to be choises of logging in or registering
    response = client.get('/')
    assert b"Log In" in response.data
    assert b"Register" in response.data

    # After logging in, there suppose to be a choice of logging out,
    # the test blog (title/body), and an 'update' choice
    auth.login()
    response = client.get('/')
    assert b'Log Out' in response.data
    assert b'test title' in response.data
    assert b'by test on 2018-01-01' in response.data
    assert b'test\nbody' in response.data
    assert b'href="/1/update"' in response.data


def test_create(client, auth, app):
    auth.login()
    assert client.get('/create').status_code == 200
    client.post('/create', data={'title': 'created', 'body': ''})

    with app.app_context():
        db = get_db()
        count = db.execute('SELECT COUNT(id) FROM post').fetchone()[0]
        assert count == 2


def test_update(client, auth, app):
    auth.login()
    assert client.get('/1/update').status_code == 200
    client.post('/1/update', data={'title': 'updated', 'body': ''})

    with app.app_context():
        db = get_db()
        post = db.execute('SELECT * FROM post WHERE id = 1').fetchone()
        assert post['title'] == 'updated'


@pytest.mark.parametrize('path', (
    '/create',
    '/1/update',
))
def test_create_update_validate(client, auth, path):
    # User with id=2 does not exist in the database
    # Response is supposed to be 404 - Not Found
    auth.login()
    response = client.post(path, data={'title': '', 'body': ''})
    assert b'Title is required.' in response.data


def test_delete(client, auth, app):
    # Delete should redirect to the main blog page
    auth.login()
    response = client.post('/1/delete')
    assert response.headers['Location'] == '/'

    # Deleted post should not be found in database
    with app.app_context():
        db = get_db()
        post = db.execute('SELECT * FROM post WHERE id = 1').fetchone()
        assert post is None