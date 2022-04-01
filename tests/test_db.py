import sqlite3

import pytest
from flaskr.db import get_db


def test_get_close_db(app):
    # get_db should return exactly the same value every time
    with app.app_context():
        db = get_db()
        assert db is get_db()

    # Test that db execution fails, since db is outside of app_context and is closed
    with pytest.raises(sqlite3.ProgrammingError) as e:
        db.execute('SELECT 1')

    # Outside of app_context, the db should be closed
    assert 'closed' in str(e.value)


def test_init_db_command(runner, monkeypatch):
    class Recorder(object):
        called = False

    def fake_init_db():
        Recorder.called = True

    # Test CLI custom command init-db
    # Substitute init_db method with a fake method that keeps track of variable 'called'
    monkeypatch.setattr('flaskr.db.init_db', fake_init_db)
    result = runner.invoke(args=['init-db'])
    assert 'Initialized' in result.output
    assert Recorder.called