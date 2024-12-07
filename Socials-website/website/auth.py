from flask import Blueprint, render_template

auth = Blueprint ('auth', __name__)

@auth.route('/Login')
def login():
    return render_template("login.html")

@auth.route('/Sign-Up')
def Signup():
    return render_template("Sign-up.html")