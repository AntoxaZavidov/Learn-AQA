import requests

payload = {"name":"Anton"}
response = requests.get("https://playground.learnqa.ru/api/hello", params = payload)
print(response.text)
print(response.status_code)