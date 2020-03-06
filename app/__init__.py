# coding=utf-8

from flask import Flask

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

    # @app.before_request       # 测试在初始化这里进行拦截,如果是login或者注册则不验证token
    # def xx():
    #     pass

    return app