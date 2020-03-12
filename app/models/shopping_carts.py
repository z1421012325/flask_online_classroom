# coding=utf-8
import datetime
from OnlineClassroom.app.ext.plugins import db
from .curriculums import *
"""
购买记录
CREATE TABLE `shopping_carts` (
  `aid` int DEFAULT NULL COMMENT '外键 用户id',
  `cid` int DEFAULT NULL COMMENT '外键 课程id',
  `number` int DEFAULT '1' COMMENT '课程数量,但是是网易云课堂类似的,默认就是1买把...',
  `create_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '创建时间',
  KEY `uid` (`aid`),
  KEY `cid` (`cid`),
  CONSTRAINT `shopping_carts_ibfk_1` FOREIGN KEY (`aid`) REFERENCES `accounts` (`aid`),
  CONSTRAINT `shopping_carts_ibfk_2` FOREIGN KEY (`cid`) REFERENCES `curriculums` (`cid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
"""


class ShoppingCarts(db.Model):
    __tablename__ = "shopping_carts"

    aid = db.Column(db.Integer,db.ForeignKey("accounts.aid"),primary_key=True, comment="外键 用户id")
    cid = db.Column(db.Integer,db.ForeignKey("curriculums.cid"),primary_key=True,comment="外键 课程id")
    number = db.Column(db.Integer,default=1)
    create_at = db.Column(db.DateTime,default=datetime.datetime.utcnow(),comment="创建时间")

    curriculum = db.relationship(Curriculums,backref="shops")

    def __repr__(self):
        return "数据库{}".format(self.__tablename__)

    def __init__(self,aid=None,cid=None):
        self.aid =aid
        self.cid = cid
        self.number = 1
        self.create_at = datetime.datetime.utcnow()


    def is_record(self):
        self.query.filter_by(aid=self.aid,cid=self.cid).first()
        if self.number != 1:
            if not self.curriculum.price <= float(0):
                return False
            return True
        return True

    def get_curriculum__catalog(self):

        items = {}
        list_time = []

        catalogs = self.curriculum.catalogs

        for catalog in catalogs:
            item = catalog.serializetion_itme()
            list_time.append(item)

        items["datas"] = list_time
        items["len"] = len(catalogs)
        return items

    def is_purchase(self):
        shop = self.query.filter_by(aid=self.aid,cid=self.cid).first()
        return shop.number == 1

    def save(self):
        self.number = 1
        self.create_at = datetime.datetime.utcnow()
        return self.is_commit()

        # commit

    def is_commit(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except Exception as e:
            db.rollback()
            return False

    def get_purchase_curriculums(self):
        shop = self.query.filter_by(aid=self.aid).first()
        cus = shop.curriculum

        items = {}
        list_item = []

        for cu in cus:
            cu.completion_oss_img_url()
            list_item.append(cu.serialize_item())

        items["datas"] = list_item
        items["len"] = len(list_item)

        return items