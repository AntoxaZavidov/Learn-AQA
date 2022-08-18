import requests


payload = {"name": "Terminator"}
responce = requests.get("https://playground.learnqa.ru/api/hello", params=payload)
print(responce.text)


