from flask import Flask, render_template, request

app = Flask(__name__)

app.route("/index")


@app.route("/index", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        return render_template("index.html")
    else:
        return "<p>hello, test!</p>"


if __name__ == "__main__":
    app.run()