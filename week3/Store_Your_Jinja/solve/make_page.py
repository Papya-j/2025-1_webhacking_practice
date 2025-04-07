import requests

url = "http://127.0.0.1:30031"

data = {
    "name":"***name***",
    "content":"***content***"
}
response = requests.post(url=url, data=data)
print(response.text)