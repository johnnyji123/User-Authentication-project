import mysql.connector
from flask import Flask, render_template
from flask import request

db = mysql.connector.connect(
    
        host = "localhost",
        user = "root",
        password = "projects123123",
        database = "authentication_db"
    )


cursor = db.cursor()

# table user_info

app = Flask(__name__)

@app.route("/" , methods = ["GET", "POST"])
def login_page():
    return render_template("index.html")

    
if __name__ == "__main__":
    app.run(debug= True, use_reloader = False)