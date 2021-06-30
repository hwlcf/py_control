import uuid
from flask import current_app, jsonify
from flask import render_template
from flask import request
from . import admin_blu
from .models import MobileUser
from ..apps import db


@admin_blu.route("/index", methods=["GET", "POST"])
def admin():
    """admin后台首页"""
    return render_template("index.html")


#
# @admin_blu.route("/login", methods=["GET", "POST"])
# def admin_login():
#     """管理员登录页面"""
#     if request.method == "GET":
#         # 去session中获取指定的值
#         user_id = session.get("user_id", None)
#         is_admin = session.get("is_admin", None)
#         # 如果用户id存在，并且是管理员，直接跳管理后台主页
#         if user_id and is_admin:
#             return redirect(url_for("admin.admin_index"))
#         return render_template("admin/login.html")
#     # html 不写action表示提交到当前页面
#     else:
#         # 获取登录参数
#         data_dict = request.form
#         user_name = data_dict.get("user_name")
#         password = data_dict.get("password")
#         if not all([user_name, password]):
#             return render_template('admin/login.html', errmsg="参数不足")
#         try:
#             user = User.query.filter(User.user_name == user_name).first()
#         except Exception as e:
#             current_app.logger.error(e)
#             return render_template('admin/login.html', errmsg="数据查询失败")
#
#         if not user:
#             return render_template('admin/login.html', errmsg="用户不存在")
#
#         if not user.check_password(password):
#             return render_template('admin/login.html', errmsg="密码错误")
#
#         print(user.is_admin)
#         if not user.is_admin:
#             return render_template('admin/login.html', errmsg="用户权限错误")
#
#         # 登录成功
#         session["is_admin"] = True
#         session["user_id"] = user.id
#         session["user_name"] = user.user_name
#
#         # 跳转页面
#         return redirect(url_for("admin.admin_index"))


@admin_blu.route("/", methods=["GET", "POST"])
def admin_index():
    """查询数据"""
    page = request.args.get('page') or 1
    size = request.args.get('size') or 3
    page = int(page)
    size = int(size)
    data_list = []
    try:
        obj_list = MobileUser.query.filter().all()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(status=400, errmsg="数据查询失败")

    obj_list = obj_list[(page - 1) * size:page * size]
    for obj in obj_list:
        data = obj.to_dict()
        data_list.append(data)
    return jsonify(status=200, msg="success", data_list=data_list)


@admin_blu.route("/detail", methods=["GET", 'POST'])
def admin_detail():
    """sn详情页"""
    mobileuser_id = request.args.get('mobileuser_id') or request.args.get('id')
    print(type(mobileuser_id))
    try:
        obj = MobileUser.query.filter(MobileUser.id == mobileuser_id).first()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(status=400, errmsg="数据查询失败")

    data = obj.to_dict()

    return jsonify(status=200, msg="success", data=data)


@admin_blu.route("/add", methods=["GET", "POST"])
def admin_add():
    """增加sn"""
    sn_number = uuid.uuid4()
    try:
        obj = MobileUser(sn_number=sn_number)
        db.session.add(obj)
        db.session.commit()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(status=400, errmsg="数据新增失败")
    return jsonify(status=200, msg="success")


@admin_blu.route("/delete", methods=["GET", ])
def admin_delete():
    """数据删除"""
    mobileuser_id = request.args.get('mobileuser_id') or request.args.get("id")
    print(type(mobileuser_id))
    try:
        obj = MobileUser.query.filter(MobileUser.id == mobileuser_id).first()
        db.session.delete(obj)
        db.session.commit()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(status=400, errmsg="数据删除失败")
    return jsonify(status=200, msg="success")


@admin_blu.route("/update", methods=["GET", "POST"])
def admin_update():
    """数据更新"""
    data = request.json
    mobileuser_id = data.get("mobileuser_id") or data.get("id")
    sn_number = data.get("sn_number")
    print(sn_number)
    version = data.get("version")
    print(version)
    model_number = data.get("model_number")
    is_usable = data.get("is_usable")

    try:
        obj = MobileUser.query.filter(MobileUser.id == mobileuser_id).first()
        obj.sn_number = sn_number
        obj.version = version
        obj.model_number = model_number
        obj.is_usable = int(is_usable)
        db.session.commit()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(status=400, errmsg="数据更新失败")
    return jsonify(status=200, msg="success")
