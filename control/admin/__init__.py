from flask import Blueprint
from flask import redirect
from flask import request
from flask import session
from flask import url_for

admin_blu = Blueprint("admin", __name__, url_prefix="/admin")


# 使用蓝图对象，实现后台admin站点的防翻墙
# @admin_blu.before_request
# def before_request():
#     # 判断当前请求的页面是否除了ｌｏｇｉｎ以外的页面
#     if not request.url.endswith(url_for("admin.admin_login")):
#         # 从session中获取管理员的状态
#         user_id = session.get("user_id")  # 管理员用户ｉｄ
#         is_admin = session.get("is_admin")
#
#         if not is_admin:
#             """如果不是管理员，统一跳转到登录页面"""
#             return redirect(url_for("admin.admin_login"))


# 因为视图函数保存在了views.py文件中所以我们需要加载进来
from . import views
