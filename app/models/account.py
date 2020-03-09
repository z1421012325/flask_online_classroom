# coding=utf-8

import datetime
from sqlalchemy import and_,or_
from werkzeug.security import check_password_hash,generate_password_hash
from OnlineClassroom.app.ext.plugins import db

from .extracts import Extracts
from .money import Money
from .purchases import Purchases
from .shopping_carts import ShoppingCarts
from .use_collections import use_collections
from .curriculum_comments import CurriculumComments
from .curriculums import Curriculums

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
    create_at   = db.Column(db.DateTime,default=datetime.datetime.utcnow(),comment="创建时间")


    # sqlalchemy orm特有的关系条件,不存在数据库表中,只是在存在实例中
    # 第一个参数为对应模型的class类名,第二个参数在对应的类中生成一个属性,关联到这个表
    # 这种关系只存在 一对多的 '一' 中
    # PS 如果多个模型不在同一个文件中会发生错误,"找不到模型" 所以import 模型
    curriculum = db.relationship(Curriculums,backref="user", lazy="dynamic")
    comments = db.relationship(CurriculumComments,backref="user", lazy="dynamic")
    extracts = db.relationship(Extracts,backref="user", lazy="dynamic")
    money = db.relationship(Money,backref="user", lazy="dynamic")
    purchases = db.relationship(Purchases,backref="user", lazy="dynamic")
    shopping_carts = db.relationship(ShoppingCarts,backref="user", lazy="dynamic")
    use_collections = db.relationship(use_collections, backref="user", lazy="dynamic")

    DefaultUserAccountStatus     = 0       # 用户状态 0为未注册用户
    RegisteredUsersTeacherStatus = 1       # 注册用户(老師)
    RegisteredUsersStudentStatus = 2       # 注册用户(學生)
    BannedUsersStatus            = 10      # 封禁用户

    def __init__(self,nickname,username,pswd,info):
        self.nickname = nickname
        self.username = username
        self.pswd = pswd
        self.status  = self.RegisteredUsersStudentStatus
        self.info = info

    def __repr__(self):
        return "数据库{}  {} --- {}".format(self.__tablename__,self.nickname,self.username)



    def EncryptionPassword(self):
        self.pswd = generate_password_hash(self.pswd)       # 简单的加密,没有加盐值

    @classmethod
    def SetEncryptionPassword(self,pswd):
        return generate_password_hash(pswd)

    def CheckPassword(self,pswd):
       return check_password_hash(self.pswd,pswd)





    # 注册
    def registryAccount(self):
        # u = self.query.filter(self.username==self.username).first()
        # print(u)
        # if u.username == self.username:
        #     print(u.username,self.username)
        #     print(" ------存在对等----\n ----------")
        #     return False

        self.EncryptionPassword()
        if not self.is_commit():
            return False
        return True


    # 修改信息
    def modify_user_info(self,nickname,info):
        if len(nickname) != 0:
            self.nickname = nickname
        if len(info) != 0:
            self.info = info

        if not self.is_commit():
            return False
        return True


    # 修改密码
    def modify_pswd(self,old,new):
        if not self.CheckPassword(old):
            return False

        self.pswd = self.SetEncryptionPassword(new)

        if not self.is_commit():
            return False
        return True


    # commit
    def is_commit(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except Exception as e:
            db.rollback()
            return False





