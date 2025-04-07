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

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/store", methods=["POST"])
def store():
    name = request.form.get("name")
    content = request.form.get("content")
    
    if not name or not re.match(r"^[0-9a-zA-Z]+$", name):
        return "Invalid Page Name"
    
    ### validsation ###
    if re.search(r"(script|on|object|frame|embed|img|src|data|base)", content, flags=re.I):
        return "No Hack ~_~"
    
    f = open("./templates/uploads/"+name+".html", "w")
    f.write(content)
    f.close()
    
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
    cookie = {"name": "flag", "value": FLAG}
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
        driver.add_cookie(cookie)

        driver.get("http://127.0.0.1:5000"+url)
    except Exception as e:
        print(e)
        driver.quit()
        return False

    driver.quit()
    return True

app.run(host="0.0.0.0", port=5000)