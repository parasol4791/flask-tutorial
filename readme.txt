https://flask.palletsprojects.com/en/1.0.x/tutorial/#tutorial

venv in PowerShell is activated by venv/Scripts/activate.ps1
Make sure an execution policy is not 'Restricted', to be able to run the script

Run Flask on PS (Ctrl+C - to exit:
$env:FLASK_APP = "flaskr"
$env:FLASK_ENV = "development"
flask run

Initialize Database:
$env:FLASK_APP = "flaskr"
$env:FLASK_ENV = "development"
flask init-db

Endpoints:
/                   # the blog itself (at the root, also referred to as 'index')
/create             # create a post
/<id>/update        # it handles delete as well
/hello
/auth/register
/auth/login

To install 'flaskr' project in editable mode (to create flaskr package from setup.py and MANIFEST.in):
pip install -e .

To run tests:
pytest
Tests showing individual functions:
pytest -v
Check for test coverage:
coverage report
Covered lines (in html):
coverage html


Exiting flask shell: Ctrl+z, Enter




