from flask import Flask
from config import Config
from flask_cors import CORS
from .api.routes import api
from .models import db
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(api)
db.init_app(app)


migrate = Migrate(app, db)
CORS(app)