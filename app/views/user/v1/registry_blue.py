# coding=utf-8



from .handlers.user import user
from .handlers.curriculum import curriculum
from .handlers.teacher import teacher
from .handlers.search import search


def init_blue(app):
    app.register_blueprint(blueprint=user,url_prefix='/user')
    app.register_blueprint(blueprint=curriculum, url_prefix='/curriculum')
    app.register_blueprint(blueprint=teacher, url_prefix='/teacher')
    app.register_blueprint(blueprint=search)