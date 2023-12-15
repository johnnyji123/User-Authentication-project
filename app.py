import mysql.connector
from flask import Flask, render_template, flash, redirect, url_for
from flask import request
from flask_mail import Mail
from flask_mail import Message
import random
import string

# Connecting to database
db = mysql.connector.connect(
    
        host = "localhost",
        user = "root",
        password = "projects123123",
        database = "authentication_db"
    )

# Creating a cursor object
cursor = db.cursor()

# table user_info
# Cnfiguring Mail in Flask to send email
app = Flask(__name__)
app.config['SECRET_KEY'] = "123123123"
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'codingprojects123123@gmail.com'
app.config['MAIL_PASSWORD'] = 'password'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)

# Creating Endpoint/ function that logs in user
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
 

# Creating endpoint/function that allows user to register and allows user to verify email
@app.route("/register_user", methods = ["GET", "POST"])
def register_user():    
    if request.method == "POST":
        # once they click submit send verification email to their email
        random_token = "".join(random.choices(string.ascii_lowercase, k = 10))
        name = request.form.get("Name")
        email = request.form.get("Email")
        password = request.form.get("Password")
        
        cursor.execute("INSERT INTO user_info (Name, Email, Password, Token) VALUES (%s, %s, %s, %s)",
                      (name, email, password, random_token) )

        msg = Message("Please verify your email", sender = "codingprojects123123@gmail.com", recipients = [email]) 
        msg.body = f"http://127.0.0.1:5000/verify_email?token={random_token}"
        mail.send(msg)
            
        db.commit()
           
    return render_template("register_user.html")
   

# Extract query parameter from the url and compare it to the Token column in database
@app.route("/verify_email", methods = ["GET", "POST"])
def email_verification():
    cursor.execute("SELECT Token FROM user_info")
    token_data = cursor.fetchall()
    extract_token_url = request.args.get('token')
    
    for token in token_data:
        if token[0] == extract_token_url:
            cursor.execute("UPDATE user_info SET verified_token = 'True' WHERE Token = %s", (extract_token_url,))
            db.commit()
            return redirect("/")
                      



if __name__ == "__main__":
    app.run(debug= True, use_reloader = False)

