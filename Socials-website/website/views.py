from flask import Blueprint, render_template

views = Blueprint ('views', __name__)

@views.route('/Home')
def home():
    return render_template("home.html")

@views.route('/Videos')
def video():
    return render_template("video.html")

@views.route('/Socials')
def social():
    return render_template('social.html')