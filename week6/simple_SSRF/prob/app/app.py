from flask import Flask, request, render_template
import os, re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

app = Flask(__name__)
app.secret_key = os.urandom(32)

try:
    FLAG = open("./flag.txt", "r").read()
except:
    FLAG = "couldn't find flag"

admin_token = []

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/store", methods=["GET"])
def store():
    name = request.args.get("name")
    content = request.args.get("content")
    admin_cookie = request.cookies.get("admin_token")
    
    if not name or not re.match(r"^[0-9a-zA-Z]+$", name):
        return "Invalid Page Name"
    
    if admin_cookie in admin_token:
        f = open("./templates/uploads/"+name+".html", "w")
        f.write(content)
        f.close()
    elif re.match(r"^[0-9a-zA-Z\s]+$", content):
        f = open("./templates/uploads/"+name+".html", "w")
        f.write(content)
        f.close()
    else:
        return "Permission Denied", 403
    
    return "Success"

@app.route("/view/<page>", methods=["GET"])
def view(page):
    if not page:
        page="test"
    
    if not re.match(r"^[0-9a-zA-Z]+$", page):
        return "Invalid Page"
    
    page = "uploads/"+page+".html"
    return render_template(page)
    
@app.route("/report", methods=["GET", "POST"])
def report():
    if request.method == "GET":
        return render_template("report.html")

    if request.method == "POST":
        url = request.form.get("url")
        
        if not url:
            return "Invalid URL! Try again..."
        if re.match("http(s)?://.*", url) and not re.match("^/.*"):
            return "Invalid URL! Try again..."
        
        try:
            bot(url)
            return "report Succeed"
        except:
            return "Failed to visit URL"
    return "Unused Method!" 

def bot(url="/"):
    random_token = os.urandom(32)
    random_token = random_token.hex()
    admin_token.append(random_token)
    
    cookie1 = {"name": "flag", "value": FLAG}
    cookie2 = {"name": "admin_token", "value": random_token}
    
    try:
        options = webdriver.ChromeOptions()
        for _ in [
            "headless=new",
            "window-size=1920x1080",
            "disable-gpu",
            "no-sandbox",
            "disable-dev-shm-usage",
        ]:
            options.add_argument(_)
        service = ChromeService(executable_path="/usr/bin/chromedriver")
        driver = webdriver.Chrome(options=options, service=service)
        driver.implicitly_wait(3)
        driver.set_page_load_timeout(20)
        driver.get("http://127.0.0.1:5000")
        driver.add_cookie(cookie1)
        driver.add_cookie(cookie2)

        driver.get("http://127.0.0.1:5000"+url)
    except Exception as e:
        print(e)
        driver.quit()
        admin_token.remove(random_token)
        return False
    driver.quit()
    admin_token.remove(random_token)
    return True

app.run(host="0.0.0.0", port=5000)