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

# ====================================================================
# ====================================================================
@app.route('/login')
def login_form():
    # GET
    return flask.render_template('login.html')

@app.route('/login', methods=['POST'])
def handle_login():
    # POST request to /login
    login = flask.request.form['login']
    password = flask.request.form['password']
    user = models.User.query.filter_by(login=login).first()
    if user is not None:
        pass_hash = bcrypt.hashpw(password.encode('utf8'), user.pass_hash)
        if pass_hash == user.pass_hash:
            flask.session['auth_user'] = user.id
            #redirect to the page which the user trys to login on
            #return flask.redirect(flask.url_for('index')) #this work but is fixed to 'index'
            # NOTE: this requires url to be set in the html butten "/login?url={{ request.path }}"
            return flask.redirect(flask.request.form['url'], 303) #  <a href="/login?url={{ request.path }}" class="pure-button login">Log In</a>

    return flask.render_template('login.html', state='bad')

@app.route('/logout')
def handle_logout():
    del flask.session['auth_user']
    return flask.redirect(flask.request.args.get('url', '/'), 303)


# --------------------------------------------------------------------
@app.route('/newUser')
def form_newUser():
    return flask.render_template('newUser.html',state = 'first')

@app.route('/newUser', methods=['POST'])
def handle_newUser():
    userName = flask.request.form['user']
    password1 = flask.request.form['password1']
    password2 = flask.request.form['password2']

    if password1 != password2:
        return flask.render_template('newUser.html',state='matchpw')
    if (len(userName)) > 20:
        return flask.render_template('newUser.html',state = 'usernametoolong')
    existing = models.User.query.filter_by(login=userName).first()
    if existing is not None:
        return flask.render_template('newUser.html',state = 'usernameistaken')
    user = models.User()
    user.login = userName
    user.pass_hash = bcrypt.hashpw(password1.encode('utf8'),bcrypt.gensalt(15))
    db.session.add(user)
    db.session.commit()
    flask.session['auth_user'] = user.id

    return flask.redirect(flask.request.form['url'],303)

# ====================================================================
# ====================================================================