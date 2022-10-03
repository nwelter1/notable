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

# Example API Calls

Endpoint `GET`: `/api/doctors`

Return Value: 
```
[
    {
        first_name: "Nate",
        id: "Cq6yAHfy1XTrOmV22E3cEf07rKjwW02J5F2ES1H5FlA",
        last_name: "Welter"
    },
    {
        first_name: "Sam",
        id: "8DUhzmFIUl-YfvNpyfBHD3SbGtcuYW4kVg5lQfJfd60",
        last_name: "Davitt"
    },
    {
        first_name: "Nicole",
        id: "00ASzT_ivowXOtRZliOOHJdj1LPXp0vdEFdsGe_aRtk",
        last_name: "Shannon"
    }
]
```

Endpoint `GET`: `api/doctors/Cq6yAHfy1XTrOmV22E3cEf07rKjwW02J5F2ES1H5FlA/12-1-2022`

Return Value: 
```
[
    {
        date: "12/1/2022 8:00 AM",
        doctor_id: "Cq6yAHfy1XTrOmV22E3cEf07rKjwW02J5F2ES1H5FlA",
        first_name: "Nate",
        id: "wUshpHYy0Qwt5V7xh1_Eg9mxHyGx2y-vo15Rr_12Epg",
        kind: "New Patient",
        last_name: "double u",
        time: "2022-12-01T08:00:00"
    },
    {
        date: "12/1/2022 8:00 AM",
        doctor_id: "Cq6yAHfy1XTrOmV22E3cEf07rKjwW02J5F2ES1H5FlA",
        first_name: "Jesse",
        id: "rZ7FZlYMyTjEi-JqUfj8ri0UcGgjTKBYpGQ6AvqZ4Z4",
        kind: "Follow-Up",
        last_name: "Plemons",
        time: "2022-12-01T08:00:00"
    },
    {
        date: "12/1/2022 8:00 AM",
        doctor_id: "Cq6yAHfy1XTrOmV22E3cEf07rKjwW02J5F2ES1H5FlA",
        first_name: "Ripal",
        id: "pcqI5Rpz03ZEbC-dUYj2b5D1vbDR0xdoKKb9-C3wXxI",
        kind: "New Patient",
        last_name: "Patel",
        time: "2022-12-01T08:00:00"
    }
]

```

Endpoint `POST` : `/api/appointments`

Body = 
```
{
	"first_name": "CT",
	"last_name": "JS Drone",
	"kind": "Follow-Up",
	"date": "12/1/2022 8:00 AM",
	"time": "12/1/2022 8:00 AM",
	"doctor_id": "Cq6yAHfy1XTrOmV22E3cEf07rKjwW02J5F2ES1H5FlA"
}
```