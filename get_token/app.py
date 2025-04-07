from flask import Flask, request
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route("/", methods=["GET"])
def index():
    pass
    
app.run(host="0.0.0.0", port=5000)