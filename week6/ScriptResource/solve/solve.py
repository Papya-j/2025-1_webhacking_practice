import requests

url = "http://127.0.0.1:30032/report"
data = {
    "url":"/view/vuln"
}
response = requests.post(url=url, data=data)
print(response.text)