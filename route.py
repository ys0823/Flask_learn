from flask import url_for, Flask

app = Flask(__name__)


# 分页
@app.route('/')
def index():
    return 'index'


@app.route('/login')
def login():
    return 'login'


# 前端变量输入
@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'


with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))