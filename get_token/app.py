from flask import Flask, request
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)

token_collector = {}

@app.route("/", methods=["GET"])
def index():
    return "main page"


@app.route("/<token>", methods=["GET"])
def token(token):
    print(token)
    try:
        data = token_collector[token]
    except:
        token_collector[token] = [request.cookies, request.args]
        return "no data"
    token_collector[token] = [request.cookies, request.args]
    return data
    
app.run(host="0.0.0.0", port=5000)