import flask
from init import  app, socketio, db
import models
import flask_sqlalchemy

@app.route('/')
def index():
    return flask.render_template('index.html',)
    # return flask.render_template('index.html', messages=messages) #example

@app.route('/login', methods=['post'])
def login():
    print('test0')
    uName = flask.request.form['uName']
    pWord = flask.request.form['pWord']

    #if username or passord empty
    if (uName is None) or (pWord is None):
        print ('missing an input')
        #return login(index)
        return flask.render_template('index.html')

    print('start query test')
    user = models.User.query.filter_by(username=uName).first()
    if user is None:
        return flask.render_template('index.html')
    if user.username == uName and user.password == pWord:
        print('logged in')
        # return/redirect loggedIn
        return flask.render_template('loggedIn.html', )
    else:
        print('login failed')
        # return/redirect login(index)
        return flask.render_template('index.html')
        #with username still filled in ... session?

    print('end login test')
    return flask.render_template('loggedIn.html', )

@app.route('/newUser', methods=['post'])
def newUser():
    #if username doesnt already exist
    uName = flask.request.form['uName']
    pWord = flask.request.form['pWord1']
    u = models.User()
    u.username = uName
    u.password = pWord
    db.session.add(u)
    db.session.commit()
        #return/redirect to login(index) pg with username filled in
    #else username does exist
        #return/redirect to newuser pg

    return flask.render_template('loggedIn.html', )