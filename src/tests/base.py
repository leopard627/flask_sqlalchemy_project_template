
from src.flaskr import app, db
from mixer.backend.flask import mixer

import unittest


class BaseTestCase(unittest.TestCase):
    # def create_app(self):
        # app.config.from_object('src.settings.TestingConfig')
        # return app

    def setUp(self):
        app.config.from_object('src.settings.TestingConfig')
        app.config['TESTING'] = True
        # self.app = app.test_client()
        mixer.init_app(app)
        self.client = app.test_client()

        db.drop_all()
        db.create_all()

    def tearDown(self):
        pass
