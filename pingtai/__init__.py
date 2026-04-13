from flask import Flask


def create_app():
    app = Flask(__name__)
    app.secret_key = 'sdfsdf789ajasd8iawnkj'

    # 导入蓝图
    from .views import account
    from .views import order

    # 注册蓝图
    app.register_blueprint(account.ac)
    app.register_blueprint(order.od)
    

    return app
