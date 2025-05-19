import requests

url = "http://127.0.0.1:30032/store"

data = {
    "name":"***page name here***",
    "content":"***content here***"
}
response = requests.get(url=url, params=data)
print(response.text)