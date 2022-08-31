from json.decoder import JSONDecodeError
import requests

response = requests.get("https://playground.learnqa.ru/api/get_text")
print(response.text)

try:
    parsed_response_text = response.json()
    print(parsed_response_text["answer"])
    print(response.status_code)
except JSONDecodeError:
    print("Response is not JSON format")