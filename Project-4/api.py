import flask
from init import app, db
import models


@app.route('/api/update_thumbs_up', methods=['POST'])
def update_thumbs_up():
    return 0