from flask import Flask
from flask import request
from flask import render_template

midterm = Flask(__name__)

@midterm.route('/')
def mlogin():
    return render_template("login.html")

if __name__ == '__main__':
    midterm.run(host='0.0.0.0', port=5000)