import json.decoder

from requests import Response
class BaseCase:
    def get_cookie (self, response: Response, cokkie_name):
        assert cokkie_name in response.cookies, f"Cannot find cookie with name {cokkie_name} in the last response"
        return  response.cookies[cokkie_name]

    def get_header (self, response: Response, headers_name):
        assert headers_name on response.headers, f"Cannot find header with name {headers_name} in the last response"
        return response.headers[headers_name]

    def get_json_value(self, response: Response, name):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"

        assert name in response_as_dict, f"Response JSON doesn't have key '{name}'"
        return response_as_dict[name]