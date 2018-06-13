from flask import Flask

myapp = Flask(__name__)

@myapp.route("/")
def testing():
    return "Welcom to my test flask"
