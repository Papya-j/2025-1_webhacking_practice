import requests

url = "http://scriptresource.ty0507.xyz/store"

name = "asdf9"
data = {
    "name":name,
    "content":"""
    """
}

response = requests.get(url=url, params=data)
print(response.text)

url = "http://scriptresource.ty0507.xyz/get_raw/"+name
data = {
    
}
response = requests.get(url=url, params=data)
print(response.text)