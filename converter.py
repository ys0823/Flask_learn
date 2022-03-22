# 自定义转换器
from werkzeug.routing import BaseConverter
from flask import Flask

app = Flask(__name__)


class RegexConverter(BaseConverter):
    def __init__(self, url_map, regex):
        super(RegexConverter, self).__init__(url_map)
        self.regex = regex

    def to_python(self, value):
        print("to_python method")
        return value


app.url_map.converters["re"] = RegexConverter


@app.route('/index/<re("1\d{10}"):value>') # 正则, 首字母开头有10位
def index(value):
    print(value)
    return "hello"


if __name__ == "__main__":
    app.run()
    # 前端访问http://127.0.0.1:5000/index/12345678910

