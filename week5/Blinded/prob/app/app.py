from flask import Flask, request, render_template
import sqlite3
import os
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
        cursor.execute(f"INSERT INTO users VALUES(\"guest\" , \"guest\");")
        conn.commit()
    conn.close()

DEFAULT_RETURN = """
    <h1>BruteForce</h1>
    """

@app.route("/", methods=["GET"])
def index():
    password = request.args.get("password")
    
    if not password:
        password = "guest"
    
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute(f"SELECT username, password FROM users WHERE password='{password}';")
        username = cursor.fetchone()
        conn.close()
    except:
        conn.close()
        return DEFAULT_RETURN
    
    return DEFAULT_RETURN


db_init()
app.run(host="0.0.0.0", port=5000)