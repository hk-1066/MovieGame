from init import db, app

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20))
    password = db.Column(db.String(64))

db.create_all(app=app)

# notes on how to query!!!!!!!!!!!!!!!!!!
# query = (model.Session.query(model.Entry)
#          .join(model.ClassificationItem)
#          .join(model.EnumerationValue)
#          .filter_by(id=c.row.id)
#          .order_by(model.Entry.amount)  # This row :)
#          .all() )