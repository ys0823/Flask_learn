# 模板jinjia2
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/index")
def index():
    # 返回data
    data = {
        "name": "zhangsan",
        "age": 18,
        "mylist": [1, 2, 3, 4, 5]
    }
    return render_template("index2.html", data=data)


def list_step(lis):
    """
    自定义过滤器
    :param lis:
    :return:
    """
    return lis[::2]


app.add_template_filter(list_step, "mylist")


if __name__ == "__main__":
    app.run()