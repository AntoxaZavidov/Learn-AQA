import requests

class TestUserAuth:
    def test_auth_user(self):
        data = {
            'email':'antoxafeniks@uandex.ru',
            'password':'123654'
        }

        response1 = requests.post("https://profile.onliner.by/sdapi/notifications/broadcasting/auth", data=data)

        print(response1.text)
        print(response1.status_code)
        print(response1.cookies)

        assert "auth_sid" in response1.cookies, "bla bla bla"
        assert "x-csrf-token" in response1.headers, "bla bla"
        assert "user_id" in response1.json(), "bla"


        auth_sid = response1.cookies.get("auth_sid")
        token = response1.headers.get("x-csrf-token")
        user_id_from_auth_method = response1.json()["user_id"]
















