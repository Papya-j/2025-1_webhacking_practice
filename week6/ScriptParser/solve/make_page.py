import requests

url = "http://127.0.0.1:30031/store"

data = {
    "name":"***name here***",
    "content":"***content here***"
}
response = requests.get(url=url, params=data)
print(response.text)