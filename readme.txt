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

Local Routes:
http://127.0.0.1:5000/hello
/auth/register
/auth/login


Exiting flask shell: Ctrl+z, Enter




