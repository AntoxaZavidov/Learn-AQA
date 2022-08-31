import requests

payload = {"email":"zavidov2@alarstudios.com", "password": "Password_1"}
response = requests.get("https://qa02.happify.com/admin/", params=payload)


print(response.status_code)
print(dict(response.cookies))