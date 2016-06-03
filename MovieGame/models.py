from init import db, app

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    login = db.Column(db.String(20))
    pass_hash = db.Column(db.String(64))
    bio = db.Column(db.String(100))
    location = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    image = db.Column(db.BLOB)
    image_type = db.Column(db.String(5))

db.create_all(app=app)

# notes on how to query!!!!!!!!!!!!!!!!!!
# query = (model.Session.query(model.Entry)
#          .join(model.ClassificationItem)
#          .join(model.EnumerationValue)
#          .filter_by(id=c.row.id)
#          .order_by(model.Entry.amount)  # This row :)
#          .all() )