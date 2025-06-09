from flask import Flask, request, render_template, Response
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
    
    if not name or not re.match(r"^[0-9a-zA-Z]+$", name):
        return "Invalid Page Name"
    
    filter = ["g", "\\137","\\x5f", "[", "]", ".", "_"]
    for i in filter:
        if i in content:
            return "No Hack"
    
    f = open("./templates/uploads/"+name, "w")
    f.write(content)
    f.close()
    
    return "Success"

@app.route("/view/<page>", methods=["GET"])
def view(page):
    if not page:
        page="test"
    
    if not re.match(r"^[0-9a-zA-Z]+$", page):
        return "Invalid Page"
    
    f = open("./templates/uploads/"+page, "r")
    data = f.read()
    f.close()
    return f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="Content-Security-Policy" content="default-src 'self'">
</head>
<body>
    {data}
</body>
</html>
"""
    
@app.route("/get_raw/<page>", methods=["GET"])
def get_raw(page):
    if not page:
        page="test"
    
    if not re.match(r"^[0-9a-zA-Z]+$", page):
        return "Invalid Page"
    
    page = "uploads/"+page
    return Response(render_template(page), mimetype='text/plain')
    
app.run(host="0.0.0.0", port=5000)