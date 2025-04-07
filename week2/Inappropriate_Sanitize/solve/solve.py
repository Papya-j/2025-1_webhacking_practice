import requests

data = {
    ***EXPLOIT DATA***
}

response = requests.***METHOD***("http://127.0.0.1:30032/***ENDPOINT***", data=data)
print(response.text)