# project/tests/test_config.py
import os
import pytest

from src.tests.base import BaseTestCase

class TestSimpleView(BaseTestCase):

    @pytest.mark.skip(reason="skip it for a moment")
    def test_smoke_test(self):
        # app.config.from_object('project.config.TestingConfig')
        self.app.config.from_object('src.settings.TestingConfig')
        assert self.app.config['DEBUG']
        assert self.app.config['TESTING']
        assert not self.app.config['PRESERVE_CONTEXT_ON_EXCEPTION']
        assert self.app.config['SQLALCHEMY_DATABASE_URI'] == os.environ.get(
            'DATABASE_TEST_URL')


@pytest.mark.skip(reason="skip it for a moment")
def test_development_config(app):
    app.config.from_object('project.config.DevelopmentConfig')
    assert app.config['DEBUG']
    assert not app.config['TESTING']
    assert app.config['SQLALCHEMY_DATABASE_URI'] == os.environ.get(
        'DATABASE_URL')


@pytest.mark.skip(reason="skip it for a moment")
def test_testing_config(app):
    # app.config.from_object('project.config.TestingConfig')
    self.app.config.from_object('src.settings.TestingConfig')
    assert self.app.config['DEBUG']
    assert self.app.config['TESTING']
    assert not self.app.config['PRESERVE_CONTEXT_ON_EXCEPTION']
    assert self.app.config['SQLALCHEMY_DATABASE_URI'] == os.environ.get(
        'DATABASE_TEST_URL')

@pytest.mark.skip(reason="skip it for a moment")
def test_production_config(app):
    app.config.from_object('project.config.ProductionConfig')
    assert not app.config['DEBUG']
    assert not app.config['TESTING']
    assert app.config['SQLALCHEMY_DATABASE_URI'] == os.environ.get(
        'DATABASE_URL')
