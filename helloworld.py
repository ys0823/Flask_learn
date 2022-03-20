from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>hello, world!</p>"


@app.route("/test")
def hello_test():
    return "<p>hello, test!</p>"


@app.route("/test_args")
def hello_test():
    return "<p>hello, test!</p>"
