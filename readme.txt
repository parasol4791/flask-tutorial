https://flask.palletsprojects.com/en/1.0.x/tutorial/#tutorial

venv in PowerShell is activated by venv/Scripts/activate.ps1
Make sure an execution policy is not 'Restricted', to be able to run the script

Run Flask on PS (Ctrl+z, Enter - to exit:
$env:FLASK_APP = "flaskr"
$env:FLASK_ENV = "development"
flask run


Local Routes:
http://127.0.0.1:5000/hello




