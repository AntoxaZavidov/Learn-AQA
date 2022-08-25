import requests


payload = {"login": "zavidov+lvtest151011@alarstudios.com", "pass": "Password_1"}
response = requests.post("https://stage.happify.com/login", data=payload)

print(response.text)
print()
print(response.status_code)
print()
print(response.cookies)


