import os
import unittest
import tempfile

import MovieGame
from init import app, db
from models import User


class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        # http://kronosapiens.github.io/blog/2014/07/29/setting-up-unit-tests-with-flask.html
        app.config.from_pyfile('settings.py')
        db.session.close()
        db.drop_all()
        db.create_all()

    def test_lookup(self):
        user = User(username='test', password='test123')
        db.session.add(user)
        db.session.commit()
        users = User.query.all()
        assert user in users
        print("number of users: %s" % len(users))

        # http://flask.pocoo.org/docs/0.11/testing/
        # self.db_fd, MovieGame.app.config['DATABASE'] = tempfile.mkstemp()
        # MovieGame.app.config['TESTING'] = True
        # self.app = MovieGame.app.test_client()
        # with MovieGame.app.app_context():
        #     MovieGame.init_db()

    # def tearDown(self):
    #     os.close(self.db_fd)
    #     os.unlink(MovieGame.app.config['DATABASE'])

    # def test_empty_db(self):
    #     rv = self.app.get('/')
    #     assert b'No entries here so far' in rv.data

if __name__ == '__main__':
    unittest.main()