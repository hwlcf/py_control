from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from control.admin.models import User
from control.apps import create_app, db
from flask_cors import CORS

CONFIG = "development"  # 选择开发，生产模式 ProductionConfig
# 创建 app，并传入配置模式：development / production
app = create_app(CONFIG)
# 解决跨域
CORS(app, resources={r"/*": {"origins": "*"}})

# Flask-script
manager = Manager(app)
# 数据库迁移
Migrate(app, db)
# 给终端脚本工具新增数据迁移的相关命令
manager.add_command('db', MigrateCommand)


@manager.option('-n', '-name', dest='name')
@manager.option('-p', '-password', dest='password')
def createsuperuser(name, password):
    """创建管理员用户"""
    if not all([name, password]):
        print('参数不足')
        return

    user = User()
    user.mobile = name
    user.user_name = name
    user.password = password
    user.is_admin = True

    try:
        db.session.add(user)
        db.session.commit()
        print("创建成功")
    except Exception as e:
        print(e)
        db.session.rollback()


if __name__ == '__main__':
    print("测试")
    manager.run()
