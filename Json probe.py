import json
import requests

responce = requests.get("https://stage.happify.com/api/happifiers/topics/")
print(responce.text)

string_as_json_format = responce.text
obj = json.loads(string_as_json_format)

print(obj['human_url'])


