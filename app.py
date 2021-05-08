from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email

app=Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgres123@localhost/phone_collector'
app.config['SQLALCHEMY_DATABASE_URI']='postgres://stebgkranopbmc:4ef0777444f7db9f0ddbe691ef521b65736cff15fb5436a6ef4e880eb9fea728@ec2-34-237-89-96.compute-1.amazonaws.com:5432/dckbm0fufh15l?sslmode=require'
db=SQLAlchemy(app)

class Data(db.Model):
    __tablename__="data"
    id=db.Column(db.Integer, primary_key=True)
    email_=db.Column(db.String(120), unique=True)
    phone_=db.Column(db.Integer)

    def __init__(self, email_, phone_):
        self.email_=email_
        self.phone_=phone_

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods=["POST"])
def success():
    if request.method=="POST":
        email=request.form["email_name"]
        phone=request.form["phone_number"]
        print(email, phone)
        if db.session.query(Data).filter(Data.email_==email).count() == 0:
            data=Data(email, phone)
            db.session.add(data)
            db.session.commit()
            send_email(email)
            return render_template("success.html")
    return render_template("index.html",
    text="This email was used previously. Please try another email.")

if __name__ == "__main__":
    app.debug=True
    app.run()