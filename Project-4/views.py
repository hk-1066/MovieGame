import os
import base64
import flask
import bcrypt
from sqlalchemy import desc
from sqlalchemy.orm import joinedload
from init import app, db
import models
import flask
from flask import Flask
import markdown
from markupsafe import Markup
import os
# import json
import time
import base64

q_list = []

@app.before_request
def setup_csrf():
    # make a cross-site request forgery preventing token
    if 'csrf_token' not in flask.session:
        flask.session['csrf_token'] = base64.b64encode(os.urandom(32)).decode('ascii')



@app.before_request
def setup_user():
    if 'auth_user' in flask.session:
        user = models.User.query.get(flask.session['auth_user'])
        flask.g.user = user


# todo: need to link question to question/answer page
@app.route('/')
def index():
    return flask.render_template('index.html',)


