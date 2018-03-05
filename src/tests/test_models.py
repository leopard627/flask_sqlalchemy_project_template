# -*- coding: utf-8 -*-


from src.models import User
from mixer.backend.flask import mixer

from src.tests.base import BaseTestCase

class TestSimpleModels(BaseTestCase):

    def test_create_fake_users(self):
        user = mixer.blend(User)
        assert User.query.all()  is not None
        assert User.query.count() is not 0

    def test_is_auto_deleted(self):
        assert User.query.count() is 0

