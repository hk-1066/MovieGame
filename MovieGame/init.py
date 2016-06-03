import flask_sqlalchemy
from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
app.config.from_pyfile('settings.py')
db = flask_sqlalchemy.SQLAlchemy(app) #settings.py: SQLALCHEMY_DATABASE_URI = 'sqlite:///QA.db' #models.py: (cant be empty, must have elements and atraburtes)db.create_all(app=app) #run manage.py, then QA.db will eventryaly appear #left click QA.db the click 'As Data Source...'
socketio = SocketIO(app)
