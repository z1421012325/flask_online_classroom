# coding=utf-8

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from sqlalchemy import create_engine

db = SQLAlchemy()
original_db = None              # 原生sql执行把柄


def create_engine_(sql):
    engine = create_engine(
        sql,
        max_overflow=0,  # 超过连接池大小外最多创建的连接
        pool_size=5,  # 连接池大小
        pool_timeout=30,  # 池中没有线程时，最多等待的时间，超时报错，默认30秒
        pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置），-1代表永远不回收，即一直被重用
    )
    return engine



# 第三方插件初始化
def ext_init(app):
    CORS(app)
    db.init_app(app)
    Migrate(app=app,db=db)

    original_db = create_engine(app.config.get('SQLALCHEMY_DATABASE_URI'))
    