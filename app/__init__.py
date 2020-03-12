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

    @app.errorhandler(500)
    def app_500_err_res(err):
        print(err)
        return "web err 500"

    @app.errorhandler(404)
    def app_404_err_res(err):
        print(err)
        return "web err 404"

    return app