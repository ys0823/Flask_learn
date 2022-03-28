from flask import Flask, render_template, request
from wtforms import StringField, PasswordField, SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, EqualTo

app = Flask(__name__)
app.config["SECRET_KEY"] = "shshs"


# 自定义表单
class Register(FlaskForm):
    username = StringField(label="用户名", validators=[DataRequired("用户名不能为空")])
    password = PasswordField(label="密码1", validators=[DataRequired("密码不能为空")])
    password2 = PasswordField(label="密码2", validators=[DataRequired("密码不能为空"), EqualTo("password")])
    submit = SubmitField(label="提交")


@app.route("/register", methods=["POST", "GET"])
def register():
    form = Register()
    if request.method == "GET":
        return render_template("register.html", form=form)
    if request.method == "POST":
        if form.validate_on_submit():  # 验证器
            user_name = form.username.data  # 打印数据
            password = form.password.data
            password2 = form.password2.data
            print(user_name, password, password2)
        else:
            print("验证失败")
        return render_template("register.html", form=form)


if __name__ == "__main__":
    app.run()