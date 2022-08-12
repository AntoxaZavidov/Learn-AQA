import json
import requests

responce = requests.get("https://qa07.happify.com/api/happifiers/4578/")
print(responce.text)

string_as_json_format = responce.text
obj = json.loads(string_as_json_format)

print(obj['human_url'])
print(obj['modified_at'])
print(obj['sponsor'])

