from init import db, app


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    login = db.Column(db.String(20))
    pass_hash = db.Column(db.String(64))


db.create_all(app=app)
