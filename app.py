import mysql.connector
from flask import Flask, render_template, flash, redirect, url_for
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
app.secret_key = "123123123"

@app.route("/" , methods = ["GET", "POST"])
def login_user():
    email = request.form.get("Email")
    password = request.form.get("Password")
    
    cursor.execute("SELECT Email, Password FROM user_info")
    data = cursor.fetchall()

    for x in data:
        if email == x[0] and password == x[1]:
            flash("You have logged in successfully")
            return render_template("logged_in.html")
        
            
    
    flash("Incorrect credentials")
    return render_template("index.html")    
 

@app.route("/register_user", methods = ["GET", "POST"])
def register_user():
    # once they click submit send verification email to their email
    return render_template("register_user.html")


@app.route("/", methods = ["GET", "POST"])
def email_verification():
    name = request.form.get("Name")
    email = request.form.get("Email")
    password = request.form.get("Password")
    
    cursor.execute("INSERT INTO user_info (Name, Email, Password) VALUES (%s, %s, %s)"
                   , (name, email, password))
    return redirect("index.html")


if __name__ == "__main__":
    app.run(debug= True, use_reloader = False)


