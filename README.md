## Setting up this Flask App
- Creating/Activating virtualenv in Terminal/CMD:
    - Windows
        - `pyton -m venv <nameofvenv>`
        - `<nameofvenv>\Scripts\activate`
    - Mac
        - `python -m venv <nameofvenv>`
        - `source <nameofvenv>/bin/activate`
- Installing requirements into virtualenv
    - `pip install -r requirements.txt`

### Add flask environment variables in Terminal/CMD:
- Windows
    - `set FLASK_ENV=development`
    - `set FLASK_APP=<NAME-OF-PROJECT>`
- Mac
    - `export FLASK_ENV=development`
    - `export FLASK_APP=<NAME-OF-PROJECT>`


### Set up a database:
- Create a postgreSQL db and get the database URL
    - Inside of `.env` file:
        - `SQLALCHEMY_DATABASE_URI=<yourdatabaseurl>`
- in Terminal/CMD
    - `flask db init`
    - `flask db migrate`
    - `flask db upgrade`

### Starting up the server
- Terminal - `flask run`
- visit API endpoints to GET/POST/DELETE data
