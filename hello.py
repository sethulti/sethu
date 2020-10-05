from flask import Flask
hello = Flask(__name__)

@hello.route("/")
def hello():
    return "Hello, World!. Welcome to Python Language"
