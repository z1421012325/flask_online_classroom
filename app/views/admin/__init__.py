# coding=utf-8
from flask import Blueprint


admin = Blueprint('admin_api_v1',__name__)


def init_blue(app):
    app.register_blueprint(blueprint=admin)