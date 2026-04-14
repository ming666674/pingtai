from flask import Flask,request,session,redirect

def auth():
    if request.path.startswith("/static"):
        # 继续向后执行，不拦截
        return 
    
    if request.path == '/login':
        #继续向后执行，不拦截
        return
    
    user_info = session.get("user_info")
    if user_info:
        #继续向后执行，不拦截
        return 

    return redirect("/login")

def create_app():
    app = Flask(__name__)
    app.secret_key = 'sdfsdf789ajasd8iawnkj'

    # 导入蓝图
    from .views import account
    from .views import order

    # 注册蓝图
    app.register_blueprint(account.ac)
    app.register_blueprint(order.od)
    
    app.before_request(auth)
    return app
