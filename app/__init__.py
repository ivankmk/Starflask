from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
# http://flask.pocoo.org/docs/1.0/api/?highlight=app%20config#flask.Config.from_object


from app import routes
