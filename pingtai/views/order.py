
from flask import Blueprint,session,redirect,render_template
from utils import db
#蓝图对象
od = Blueprint("order", __name__)


@od.route('/order/list')
def order_list():
    user_info = session.get("user_info")
    role = user_info['role'] #1-客户  2-管理员
    if role == 2:
       # select * from order 
       # data_list = db.fetch_all("select * from `order`", [])
       data_list = db.fetch_all("select * from `order` left join userinfo on `order`.user_id = userinfo.id;", [])
    else:
        # select * from order where user_id = user_info['id']
        data_list = db.fetch_all("select * from `order` left join userinfo on `order`.user_id = userinfo.id where `order`.user_id =%s",[user_info['id'],])
    
    status_dict = {
        1:{"text":"待执行",'cls':"primary"},
        2:{"text":"正在执行",'cls':"info"},
        3:{"text":"完成",'cls':"success"},
        4:{"text":"失败",'cls':"danger"},
    }
    return render_template("order_list.html",data_list=data_list,status_dict=status_dict,real_name = user_info['real_name'])


@od.route('/order/create')
def create_list():
    return "创建订单"


@od.route('/order/delete')
def delete_list():
    return "删除订单"
