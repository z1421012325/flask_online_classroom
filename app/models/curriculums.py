# coding=utf-8

import datetime
from OnlineClassroom.app.ext.plugins import db

from .catalog import Catalog
from .curriculum_comments import CurriculumComments
from OnlineClassroom.app.utils.aliyun_oss import get_img_oss_url

"""
课程表
    CREATE TABLE `curriculums` (
    `cid` int NOT NULL AUTO_INCREMENT COMMENT '课程id',
    `cname` varchar(60) NOT NULL COMMENT '课程名字',
    `aid` int DEFAULT NULL COMMENT '外键 课程老师id',
    `price` float(10,2) DEFAULT '0.00' COMMENT '价格',
    `info` text COMMENT '课程介绍',
    `cimage` varchar(250) DEFAULT NULL COMMENT '阿里云oos直传',
    `create_at` datetime DEFAULT now() COMMENT '创建时间',
    `delete_at` datetime DEFAULT NULL COMMENT '删除时间',
    PRIMARY KEY (`cid`),
    KEY `u_id` (`uid`),
    CONSTRAINT `curriculums_ibfk_1` FOREIGN KEY (`uid`) REFERENCES `accounts` (`aid`)
    ) ENGINE=InnoDB AUTO_INCREMENT=100 DEFAULT CHARSET=utf8;
"""

class Curriculums(db.Model):
    __tablename__ = "curriculums"
    cid = db.Column(db.Integer, primary_key=True, comment="课程id")
    cname = db.Column(db.String(60), nullable=False, comment="课程名字")
    aid = db.Column(db.Integer, db.ForeignKey("accounts.aid"), comment="外键 课程老师id")
    price = db.Column(db.Float(10, 2), default=0.0, comment=" 价格")
    info = db.Column(db.Text, comment=" 课程介绍")
    cimage = db.Column(db.String(250), comment="课程封面 阿里云oos直传")
    create_at = db.Column(db.DateTime,default=datetime.datetime.utcnow(), comment="创建时间")
    delete_at = db.Column(db.DateTime, comment="删除时间")

    catalogs = db.relationship(Catalog,backref="curriculum")
    comments = db.relationship(CurriculumComments,backref="curriculum")


    def __repr__(self):
        return "数据库{}".format(self.__tablename__)

    def __init__(self,cid=None,cname=None,aid=None,price=None,info=None,cimage=None):
        self.cname = cname
        self.aid = aid
        self.price = price
        self.info = info
        self.cimage = cimage


    def completion_oss_img_url(self):
        self.cimage = get_img_oss_url(self.cimage,86400/2)

    def save(self):
        self.create_at = datetime.datetime.utcnow()
        return self.is_commit()

    def is_commit(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except Exception as e:
            db.rollback()
            return False


    # 查询多个课程并返回dict
    def query_curriculums_is_not_del(self):
        pass

    # 查询单个课程并返回dict
    def query_also_serialize(self):
        cc = self.query_curriculum_is_not_del()
        return self.serialize_item()

    def query_curriculum_is_not_del(self):
        cc = self.query.filter_by(aid=self.aid, delete_at=None).first()
        cc.completion_oss_img_url()
        return cc

    def serialize_item(self):
        item = {
            "cid": self.cid,
            "cname": self.cname,
            "aid": self.aid,
            "price": self.price,
            "info": self.info,
            "cimage": self.cimage,
            "create_at": self.create_at,
            "delete_at":self.delete_at
        }
        return item

    def query_modify_curriculum_people(self):
        self.query.filter_by(cid=self.cid,delete_at=None).first()
        return self.aid

    def modify_curriculum_info(self,name,price,info,cimage):
        self.cname = name
        self.price = price
        self.info = info
        self.cimage = cimage

        return self.is_commit()


    def recommend_curriculums(self):
        current = self.query.filter_by(cid=self.cid).first()
        aid = current.aid

        cus = self.query.filter_by(aid=aid).all()

        items = {}
        list_item = []

        for cu in cus:
            item = cu.serialize_item()
            list_item.append(item)

        items["datas"] = list_item
        items["len"] = len(cus)

        return items


    def is_identity(self,aid=None):
        cc = self.query.filter_by(cid=self.cid).first()
        return int(cc.aid) == int(aid)


    def del_curriculums(self):
        self.delete_at = datetime.datetime.utcnow()
        return self.is_commit()


    def query_del_videos(self):

        items = {}
        list_item = []

        ccs = self.query.filter(self.aid==self.aid,self.delete_at!=None).all()
        for cc in ccs:
            cc.completion_oss_img_url()
            item = cc.serialize_item()
            list_item.append(item)

        items['datas'] = list_item
        items['len'] = len(ccs)

        return items


    def recovery_curriculum(self):
        cc = self.query.filter_by(cid=self.cid,aid=self.aid).first()
        cc.delete_at = None
        return self.is_commit()

