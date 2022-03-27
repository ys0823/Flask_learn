from flask import Flask, abort, request, make_response,render_template

app = Flask(__name__)


@app.route("/index", methods=["POST", "GET"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    if request.method == "POST":
        name = request.form.get("name")
        password = request.form.get("password")
        if name == "zhangsan" and password == "123":
            return "success login"
        else:
            abort(404)  # 抛出http异常, 这里抛出404错误
            return None


# 自定义错误方法
@app.errorhandler(404)
def handle_404_error(error):
    return render_template("404.html")


if __name__ == "__main__":
    app.run()