# 2. XSS(Cross-Site Scripting)

## 1. XSS는 무엇인가?

- cross-site scripting의 약자로, 자기 자신(same-site)가 아닌 script를 실행하는 취약점
    - CSS와 이름이 겹쳐서 C대신 X를 사용함
- ‘script’, 즉 Javascript를 활용한다.
- 취약점 발생 이유
    - 유저 input 데이터에 대한 검증 미흡
    - 데이터와 코드가 분리되지 않음
- 공격 목표
    - 해당 유저의 Data를 탈취한다.
        - 예시
            1. 쿠키를 탈취하여 세션 데이터 탈취 
                - 특히 admin 계정을 탈취하면 치명적
            2. 입력 중인 id, password를 탈취
            3. 프라이버시 침해
            4. 기타 유저 행동을 감지해서 악용할 수 있는 부분들

### 1.1 Javascript가 할 수 있는 행동들

- JS는 어떠한 행동들을 할 수 있는가?
    - getElementBy Series
        1. document.getElementById("demo");
            - attribute 중 id=”demo”인 element를 가져온다.
            - 여러 개라면 맨 처음에 있는 것을 반환한다.
        2. document.getElementByClassName(”my_class”)
            - Attribute 중 class=”my_class”인 모든 element를 가져온다.
                - HTML Collection형식 : Array처럼 작동하지만, HTML Content를 가지고 있음.
            - id는 identifier → 단일하다 예측, class는 다양한 공통의 속성을 가진 친구들
        3. document.getElementByName(”test”)
            - Attribute 중 name=”test”인 모든 element를 NodeList 형식으로 전부 반환한다.
        4. document.getElementByTagName(”p”)
            - Tag의 이름”p”인 즉, <p>를 HTML Collection 형식으로 전부 반환한다.
    - document.cookie
        - cookie를 가져오는 방법
    - history
        - 기록을 확인해서 이동할 수 있다.
        - history.go(-2) : 전전 페이지로 이동

## 2. Type of XSS

- 공격 유형
    - Reflected XSS
        - 서버에 값을 요청하면서 나타나는 XSS
        - url parameter를 통해 값을 전달하면서, 이 parameter가 웹 페이지에 반영되어 javascript가 실행됨
        - 특정 user가 특정 url에 접속하면서 나타남. 광범위한 공격은 어렵지만 특정 개인에 맞춤형으로 공격을 구성하는 경우가 많음
        - 오늘 주차에서 가장 많이 볼 것
    - Stored XSS
        - 서버에 데이터가 저장됨으로써 나타나는 XSS
        - javascript data가 서버에 저장되면서 나중에 그 페이지를 불러올 때 javascript가 실행됨
        - 한 번 페이지에 업로드하면, 그 페이지에 접속하는 모든 user가 공격 대상.
    - DOM-based XSS
        - DOM은 Document Objective Model의 약자로 JS HTML의 특성을 이용해 내부 logic을 바꿔 javascript가 실행됨

## 3. 공격

- 공격 방법
    - 유저 데이터 중 페이지에 영향을 줄 수 있는 부분을 찾는다.
    - 코드가 실행되는지 확인
    - 원하는 데이터를 탈취할 수 있도록 코드를 작성한다.
- 공격 예제 : simple_xss
    - 공격 목표는 무엇인가?
        - 어떤 정보를 얻는 것이 목표인가?
    - 어디에 취약점이 있는가?
        - 웹 중 몇 번 줄에 존재하는가?
        - 어떤 type의 XSS인가?
    - 예제 exploit code 살펴보기
        1. script.py
            - 가장 기본적인 방법. javascript code를 실행시켜주는 <script>태그 이용
            - script 태그의 경우 javascript를 직접 태그 안에 넣어주는 방법과,
            - src=”{url}”의 형식으로 외부 혹은 자신의 사이트 혹은 파일에서 javascript 파일을 불러오는 방법이 존재한다.
        2. event_handler.py
            - HTML attribute 중에 event handler가 존재
            - event handler는 특정 유저 동작을 감지하여 특정 javascript를 실행시켜줌.
                - ex) onclick : 특정 element가 click되는 경우 attribute에 작성된 javascript 실행
        3. object.py
            - frame, embed, object 등의 태그는 페이지 안에 페이지를 삽입할 때 사용한다.
                - ex) blog 안에 들어간 youtube 동영상
            - 이 중 src, data attribute를 이용해서 javascript 실행 가능
                - 기본적으로 frame, embed, object는 안의 page에서 바깥 page에 접근할 수 없다.
                - url scheme 자체(javascript:{js code})로 실행시키는 경우 접근이 가능하며,
                - 안에 공격자 서버의 페이지를 띄우더라도 바깥 페이지의 cookie 등을 탈출하는 것은 불가능하다.

## 4. 보호 기법

- mitigation
    1. sanitization, validation
        - sanitization(정화) : 특정 문자열을 없애거나
            - script 태그, frame, object, embed 태그, eventhandler 등을 제거
            - 직접 만드는 경우, OWASP Java HTML Sanitizer와 같은 형식을 사용하는 경우
        - validation(검증) : 해킹 가능한 문자열일 있는지 확인하는 방식
            - script 태그, frame, object, embed 태그, eventhandler 등을 확인
    2. encode data
        - tag와 관련된 <, >과 같은 문자열을 HTML encoding을 활용하여 encode
        - <를 &lt;, >를 &gt;로 바꾸는 등
    3. use safe function
        - user input 자체를 문자열로 자동으로 취급하는 function을 이용.
    4. CSP(Content Security Policy), SOP(Same Origin Policy)
    5. HttpOnly Flag for Cookies

### 4.1 mitigation bypass

- 잘못된 / 부족한 mitigation bypass
    1. sanitization, validation
        - Lack_of_Validation1
        - Inappropriate_Sanitize
        - Lack_of_Validation2
    2. encode data
    3. use safe function
        - Safe_Renderer
    4. CSP(Content Security Policy), SOP(Same Origin Policy)
    5. HttpOnly Flag for Cookies

## 5. mitigation 관련 함수, 모듈들

- 기초지식들
    - regex(정규식)
        - 정규식:문자열이 어떻게 생겼는지 표현을 해주는 식
            - regexr.com에서 직접 테스트해볼 수 있다.
        - 다양한 특수 문자들로 여러가지 문자열을 한 번에 만족하는 식을 만들 수 있음
            - . : 어떤 문자열이든 match
            - * : 앞의 문자가 0~무한대로 반복되면 match
            - + : 앞의 문자가 1~무한대로 반복되면 match
            - [ ] : 안에 문자 중 1개만 있어도 match
                - [0-9]를 하는 경우 0~9까지 모든 ascii 문자 match
            - ^ : start match, 항상 문자열 시작이 이 문자라는 것을 보장
            - $ : end match, 항상 문자열의 끝이 이 문자라는 것을 보장
            - \w : whitespace에 대해 모두 match (space, \t, \n, 등등)
            - \d : digit에 대해 모두 match (숫자 자리수 1개)
            - 특정 문자열은 특수 문자열로 사용되므로 escape해줘야 함.
                - \(, \), \[, \] 등등
        - regex flags
            - 정규식이 match되는지 결정하는 데 특수한 조건을 표현
            - re.I ; re.IGNORECASE
                - 영어 대소문자 구분 X
            - re.A ; re.ASCII
                - unicode match를 제외하고 ascii match만 확인
            - re.M ; re.MULTILINE
                - ^와 $의 기준이 \n 앞뒤로도 적용됨
            - re.S ; re.DOTALL
                - .이 \n도 포함하도록 설정 (기본적으로 .은 \n을 포함하지 않음)
    - Jinja2 template (이하 Jinja)
        - Server-Side-Rendering(SSR)
            - 동적인 페이지를 주지만, user에서 처리하는 것이 아니라 server에서 처리하는 것이다.
            - 대체로 template들이 SSR에 해당
        - {{ }}와 {%  %}를 활용하여 template을 생성
            - variable bracket, block bracket
            - (official한 표현은 아니지만, )출력 bracket과 비출력 bracket
            - 참고로 {# #}은 comment에 사용
        - {{ 4+2 }} < python으로 취급되어 6이 출력
        - {{ text }} < 변수로 취급
            - render_template(”index.html”, text=”string”)
            - 위와 같이 변수를 전달해주어야 함.
        - js 파일 import
            - `<script src="{{ url_for('static', filename='index.js')}}"></script>`
            - static 폴더의 index.js를 가져오겠다는 의미
        - {% %}는 if문, for문 등을 사용할 때 활용
            - if, endif를 통해 해당 if state에 만족하면 안에 있는 block의 값을 출력
            - for도 비슷한 결과
1. sanitization, validation
    - re.findall()
        - regex와 match되는 모든 string을 list로 반환
    - re.search
        - regex와 match되는 모든 string을 match object로 반환
        - match object는 아래와 같은 함수, 변수가 존재
            - .span() : match string의 start index와 end index를 tuple로 묶어 반환
            - .string : 해당 함수(re.search 등)에 input으로 줬던 string 반환
            - .group() : match되는 string을 반환
    - re.sub
        - match되는 문자열 제거
        - .*와 같은 아무 문자나 반복하는 함수의 경우 생각한 것과 다르게 작동할 수도 있음
    - 그 외 re.split같은 함수도 존재
    - in 연산자
    - python string관련 함수(python string methods / python string functions로 검색)
        - upper, lower : 대문자, 소문자로 통일하여 확인
        - replace : 찾은 문자열을 다른 문자열로 변환
            - script와 같은 문자열을 empty string(””)로 치환
        - 그 외 기타 함수들.
2. encode data
    - replace : 찾은 문자열을 다른 문자열로 변환
        - “<”와 같은 문자열을 “&lt;”로 변환
3. use safe function
    - render_template()
        - jinja에서 {{  }}를 통해 감싸진 string 변수의 경우 자동으로 text로 encoding되어 나타난다.
4. CSP(Content Security Policy), SOP(Same Origin Policy)
    - 대체로 그냥 head, Header에 작성
5. HttpOnly Flag for Cookies
    - set_cookie("name", value = "value", httponly = True)