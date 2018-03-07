# -*- coding: utf-8 -*-

import json

from src.tests.base import BaseTestCase
from src.flaskr import User

from mixer.backend.flask import mixer


class TestSimpleView(BaseTestCase):

    def test_hello_world(self):
        res =self.client.get("/")
        assert res.status_code == 200

    def test_jwt_and_auth_test(self):
        # 토큰없이 시도를 할때에는 401 에러는 받습니다.
        res = self.client.get(
                "/protected",
                content_type="application/x-www-form-urlencoded")
        assert res.status_code == 401

        # Fake User을 만들어서, 해당 유저의 토큰을 발급받습니다.
        u = mixer.blend(User)
        data = json.dumps({"username": u.username, "password": u.password})
        res = self.client.post(
                    "/auth",
                    data=data,
                    content_type="application/json"
                )

        # 정상적인경우 status 200을 받습니다.
        assert res.status_code == 200
        assert 'access_token' in str(res.data)

        # 이제 헤더에 토큰을 추가해서 다시 시도합니다.
        token = json.loads(res.data)["access_token"]
        res = self.client.get(
                "/",
                headers={'Authorization': 'JWT ' + token})
        assert res.status_code == 200



