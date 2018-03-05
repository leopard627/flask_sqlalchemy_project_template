
from src.tests.base import BaseTestCase


class TestSimpleView(BaseTestCase):

    def test_hello_world(self):
        res =self.client.get("/")
        assert res.status_code == 200
