import requests


responce = requests.get("https://as.happify.com/api/happifiers/topics/")
print(responce.text)

