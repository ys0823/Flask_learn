from flask import Flask, redirect, url_for

app = Flask(__name__)


# 重定向到网站
@app.route("/index")
def index():
    return redirect("https://www.baidu.com")


# 重定向到自身路由
@app.route("/")
def hello():
    return "hello world"


if __name__ == "__main__":
    app.run()
