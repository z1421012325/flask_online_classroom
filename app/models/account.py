# coding=utf-8

import datetime
from werkzeug.security import check_password_hash,generate_password_hash

from OnlineClassroom.app.ext.plugins import db


"""
account

create table accounts (
    `aid` int primary key auto_increment comment '用户id',
    `nickname` char(20) not null comment '昵称',
    `username` char(20) not null comment '账号',
    `pswd` varchar(255) not null comment '密码',
    `status` tinyint default '0' comment '身份状态',
    `info` text comment '一些额外的信息',
    `create_at` datetime default now(),
    UNIQUE KEY `nickname` (`nickname`),
    UNIQUE KEY `username` (`username`))
    ENGINE=InnoDB AUTO_INCREMENT=10000 DEFAULT CHARSET=utf8;

"""


class Account(db.Model):

    __tablename__ = "accounts"

    aid         = db.Column(db.Integer,primary_key=True,comment="用户id")
    nickname    = db.Column(db.String(20),nullable=False,unique=True, comment="昵称")
    username    = db.Column(db.String(20),nullable=False,unique=True,comment="账号")
    pswd        = db.Column(db.String(255),nullable=False,comment="密码")
    status      = db.Column(db.Integer,comment="身份状态")
    info        = db.Column(db.TEXT,comment="一些额外的信息")
    create_at   = db.Column(db.DateTime,comment="创建时间")


    # sqlalchemy orm特有的关系条件,不存在数据库表中,只是在存在实例中
    # 第一个参数为对应模型的class类名,第二个参数在对应的类中生成一个属性,关联到这个表
    # 这种关系只存在 一对多的 '一' 中
    curriculum = db.relationship("Curriculums",db.backref("user"),db.lazyload("dynamic"))
    comments = db.relationship("CurriculumComments",db.backref("user"),db.lazyload("dynamic"))
    extracts = db.relationship("Extracts",db.backref("user"),db.lazyload("dynamic"))
    money = db.relationship("Money",db.backref("user"),db.lazyload("dynamic"))
    purchases = db.relationship("Purchases",db.backref("user"),db.lazyload("dynamic"))
    shopping_carts = db.relationship("ShoppingCarts",db.backref("user"),db.lazyload("dynamic"))
    use_collections = db.relationship("UseCollections", db.backref("user"), db.lazyload("dynamic"))

    DefaultUserAccountStatus     = 0       # 用户状态 0为未注册用户
    RegisteredUsersTeacherStatus = 1       # 注册用户(老師)
    RegisteredUsersStudentStatus = 2       # 注册用户(學生)
    BannedUsersStatus            = 10      # 封禁用户

    def __init__(self,nickname,username,pswd):
        self.nickname = nickname
        self.username = username
        self.pswd = pswd
        self.status  = self.DefaultUserAccountStatus

    def __repr__(self):
        return "数据库{}".format(self.__tablename__)

    def EncryptionPassword(self):
        self.pswd = generate_password_hash(self.pswd)       # 简单的加密,没有加盐值

    def SetEncryptionPassword(self,pswd):
        self.pswd = generate_password_hash(pswd)

    def CheckPassword(self,pswd):
       return check_password_hash(self.pswd,pswd)

    def QueryAccount(self):
        if self.nickname == "":
            return ""
        if self.username == "":
            return ""
        pass



