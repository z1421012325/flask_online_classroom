# coding=utf-8

from OnlineClassroom.app.ext.plugins import db

"""
用户金额
CREATE TABLE `money` (
  `aid` int DEFAULT NULL COMMENT '外键用户表id,唯一',
  `money` float(10,2) DEFAULT '0.00' COMMENT '金钱',
  `version` int DEFAULT NULL COMMENT '乐观锁,版本控制',
  UNIQUE KEY `aid` (`aid`),
  CONSTRAINT `money_ibfk_1` FOREIGN KEY (`aid`) REFERENCES `accounts` (`aid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
"""


class Money(db.Model):
    __tablename__ = "money"

    aid = db.Column(db.Integer,db.ForeignKey("accounts.aid"), comment="外键用户表id,唯一")
    money = db.Column(db.Float(10,2), default=0.00, comment="金钱")
    version = db.Column(db.Integer, comment="乐观锁,版本控制")

    def __repr__(self):
        return "数据库{}".format(self.__tablename__)