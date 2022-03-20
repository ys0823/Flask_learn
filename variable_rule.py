from flask import url_for, Flask

import route

app = Flask(__name__)


@app.route("/user/<float:id>")
def variable(id):
    if id == 1.0:
        return "1"
    if id == 2.0:
        return "2"
    if id == 3.0:
        return "3"
    return "hello world"


