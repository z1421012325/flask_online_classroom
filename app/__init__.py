# coding=utf-8

from flask import Flask,request,jsonify

from OnlineClassroom.app.config import conf
from OnlineClassroom.app.ext import plugins


def create_app():
    app = Flask(__name__)

    # 配置加载
    app.config.from_object(conf.env.get("a","b"))

    # 插件加载
    plugins.ext_init(app)


    # 蓝图加载...
    # 后台路由
    from OnlineClassroom.app.views import admin as admin_v1
    admin_v1.init_blue(app)
    # 面向用户的路由
    from OnlineClassroom.app.views.user.v1 import registry_blue
    registry_blue.init_blue(app)


    from OnlineClassroom.app.utils.get_token import check_token,requst_get_token
    @app.before_request
    def filter_is_token():
        print(request.path)

        not_filter = ["login","registry","register"]
        for p in not_filter:
            if p in request.path:
                print("无需检测 token")
                return None

        token = requst_get_token()
        print("\n token ",token)
        print("\n  " )
        ok,aid = check_token(token)
        if ok:
            print("token 检测成功")
            return None

        print("token 检测异常")
        return jsonify({"err":"0-0"})



    @app.errorhandler(500)
    def app_500_err_res(err):
        print(err)
        return "web err 500"

    @app.errorhandler(404)
    def app_404_err_res(err):
        print(err)
        return "web err 404"

    return app