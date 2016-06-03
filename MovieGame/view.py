import flask
from init import  app, socketio, db
import models

@app.route('/')
def index():
    return flask.render_template('index.html',)
    # return flask.render_template('index.html', messages=messages) #example