import requests

payload = {"name":"Anton"}
responce = requests.get("https://playground.learnqa.ru/api/hello", params = payload)
print(responce.text)


