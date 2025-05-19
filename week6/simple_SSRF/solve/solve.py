import requests

url = "http://127.0.0.1:30030/report"
data = {
    "url":"/view/vuln"
}
response = requests.post(url=url, data=data)
print(response.text)