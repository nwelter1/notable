from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import uuid
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
# creates a hex token for eventual API access
import secrets
# importing login manager package and user loader for our db table
from flask_login import LoginManager, UserMixin
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
login_manager = LoginManager()
ma = Marshmallow()

class Doctor(db.Model):
    id = db.Column(db.String, primary_key = True)
    first_name = db.Column(db.String(150), nullable = False)
    last_name = db.Column(db.String(150), nullable = False)
    appointment = db.relationship('Appointment', backref='owner', lazy = True)

    def __init__(self, first_name, last_name):
        self.id = self.set_id()
        self.first_name = first_name
        self.last_name = last_name

    def set_id(self):
        return (secrets.token_urlsafe())

class Appointment(db.Model):
    id = db.Column(db.String, primary_key=True)
    first_name = db.Column(db.String(150), nullable = False)
    last_name = db.Column(db.String(150), nullable = False)
    date = db.Column(db.String, nullable = False)
    time = db.Column(db.String, nullable = False)
    kind = db.Column(db.String(150), nullable = False)
    doctor_id = db.Column(db.String, db.ForeignKey('doctor.id'))

    def __init__(self, first_name, last_name, kind, date, time, doctor_id):
        self.id = self.set_id()
        self.first_name = first_name
        self.last_name = last_name
        self.kind = kind
        self.date = date
        self.time = time
        self.doctor_id = doctor_id

    def set_id(self):
        return (secrets.token_urlsafe())


class DocSchema(ma.Schema):
    class Meta:
        fields = ['id', 'first_name', 'last_name']
class ApptSchema(ma.Schema):
    class Meta:
        fields = ['id', 'first_name', 'last_name','kind','date','time', 'doctor_id']

doc_schema = DocSchema()
docs_schema = DocSchema(many=True)

appt_schema = ApptSchema()
appts_schema = ApptSchema(many=True)
