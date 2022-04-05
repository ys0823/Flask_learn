from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


class Config:
    SQLAlCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/flaskdb"
    SQLAlCHEMY_TRACK_MODIFICATIONS = True


app.config.from_object(Config)

# 数据库对象和flask绑定
db = SQLAlchemy(app)


class Role(db.Model):
    """
    创建一张角色表
    """
    __tablename__ = "role"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)


class User(db.Model):
    """
    创建一张用户表
    """
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(128))
    # 用户表和角色表关联, 通过外键关联字段id
    role_id = db.Column(db.Integer, db.ForeignKey("role.id"))


if __name__ == "__main__":
    # 创建所有表
    db.drop_all()
    # 创建所有对象
    db.create_all()
    # 创建对象 插入数据
    role1 = Role(name="admin")
    # session记录到对象任务中
    db.session.add(role1)
    # 提交事务
    db.session.commit()

    role2 = Role(name="admin2")
    db.session.add(role2)
    db.session.commit()

    use1 = User(name="zhangsan", password="123", role_id=role1.id)
    use2 = User(name="lisi", password="321", role_id=role1.id)
    user3 = User(name="wangwu", password="321", role_id=role2.id)
    db.session.add_all([use1, use2, user3])
    db.session.commit()
