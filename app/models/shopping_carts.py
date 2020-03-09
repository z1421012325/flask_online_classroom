# coding=utf-8
import datetime
from OnlineClassroom.app.ext.plugins import db

"""
购物车
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

    def __repr__(self):
        return "数据库{}".format(self.__tablename__)