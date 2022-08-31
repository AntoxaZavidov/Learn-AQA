import requests

response = requests.get("https://playground.learnqa.ru/api/get_500" )
print(response.status_code)
print(response.text)


response2 = requests.get("https://playground.learnqa.ru/api/nexta" )
print(response2.status_code)
print(response2.text)

response3 = requests.get("https://playground.learnqa.ru/api/get_301", allow_redirects=True)
first_response = response3.history[0]
secondary_response = response3
print(first_response.url)
print(secondary_response.url)
print(response3.status_code)
print(response3.text)

response4 = requests.get("https://playground.learnqa.ru/api/get_301", allow_redirects=False)
print(response4.status_code)
print(response4.text)