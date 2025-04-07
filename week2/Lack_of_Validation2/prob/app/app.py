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
    html = request.args.get("html")

    if not html:
        html = ''

    if re.search(r"(<.*script.*>|<.*on.*>|<.*frame.*>|<.*embed.*>|<.*object.*>)", html):
        return "No Hack ~_~"
    
    return f"""
    <h1>Lack of Validation</h1>
    {html}
    <br><br><br>
    If you find error, report the URL 
    <a href="/report">here</a>
    """
    
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