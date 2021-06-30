from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

from control.apps import db


class BaseModel(object):
    """模型基类，为每个模型补充创建时间与更新时间"""
    create_time = db.Column(db.DateTime, default=datetime.now)  # 记录的创建时间
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)  # 记录的更新时间


class User(BaseModel, db.Model):
    """用户"""
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)  # 用户编号
    user_name = db.Column(db.String(32), unique=True, nullable=False)  # 用户昵称
    password_hash = db.Column(db.String(128), nullable=False)  # 加密的密码
    last_login = db.Column(db.DateTime, default=datetime.now)  # 最后一次登录时间
    is_admin = db.Column(db.Boolean, default=False)

    def to_dict(self):
        """将用户对象信息转换为字典数据"""

        resp_dict = {
            "id": self.id,
            "user_name": self.user_name,
            "create_time": self.create_time.strftime("%Y-%m-%d %H:%M:%S"),
            "last_login": self.last_login.strftime("%Y-%m-%d %H:%M:%S"),
        }

        return resp_dict

    @property
    def password(self):
        raise AttributeError("当前属性不可读")

    @password.setter
    def password(self, value):
        self.password_hash = generate_password_hash(value)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class MobileUser(BaseModel, db.Model):
    """用户"""
    __tablename__ = "MobileUser"

    id = db.Column(db.Integer, primary_key=True)  # 自增id
    sn_number = db.Column(db.String(128), unique=True, nullable=False)  # sn
    version = db.Column(db.String(128), nullable=True)  # 系统版本
    model_number = db.Column(db.String(128), nullable=True)  # 手机型号
    last_login = db.Column(db.DateTime, default=datetime.now)  # 最后一次登录时间
    is_usable = db.Column(db.Boolean, default=False)  # sn是否可用

    def to_dict(self):
        """将对象信息转换为字典数据"""

        resp_dict = {
            "id": self.id,
            "sn_number": self.sn_number or None,
            "version": self.version or None,
            "model_number": self.model_number or None,
            "create_time": self.create_time.strftime("%Y-%m-%d %H:%M:%S") or None,
            # "last_login": self.last_login.strftime("%Y-%m-%d %H:%M:%S") or None,
            "is_usable": self.is_usable,
        }

        return resp_dict
