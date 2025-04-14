from flask import Flask, request, render_template
import sqlite3
import os, re
app = Flask(__name__)
app.secret_key = os.urandom(32)

DB_PATH = './db/database.db'

def db_init():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    table_check_query = "SELECT name FROM sqlite_master WHERE type='table' AND name='users'"
    cursor.execute(table_check_query)
    table_exists = cursor.fetchone()
    
    if not table_exists:
        try:
            FLAG = open("./flag.txt", "r").read()
        except:
            FLAG = "couldn't find flag"
        cursor.execute("""CREATE TABLE users(
                username TEXT NOT NULL,
                password TEXT NOT NULL);""")
        cursor.execute(f"INSERT INTO users VALUES(\"admin\" , \"{FLAG}\");")
        cursor.execute(f"INSERT INTO users VALUES(1234 , \"guest\");")
        conn.commit()
    conn.close()

@app.route("/", methods=["GET"])
def index():
    username = request.args.get("username")
    
    if not username:
        username = 1234
    
    if re.search(r"(\"|\'|\(|\)|or|and|select|union|insert|update|delete)", username, re.I):
        return "No Hack ~_~"
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(f"SELECT username, password FROM users WHERE username={username};")
    try:
        username, password = cursor.fetchone()
    except:
        conn.close()
        return "ERROR occured"
    conn.close()
    
    return f"""
    <h1>no_string</h1>
    Hello, {username}
    your password is {password}
    """

db_init()
app.run(host="0.0.0.0", port=5000)