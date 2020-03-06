# coding=utf-8

from OnlineClassroom.app.ext.plugins import db


"""
课程表
    CREATE TABLE `curriculums` (
    `cid` int NOT NULL AUTO_INCREMENT COMMENT '课程id',
    `cname` varchar(60) NOT NULL COMMENT '课程名字',
    `uid` int DEFAULT NULL COMMENT '外键 课程老师id',
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
    cid = db.Column(db.Integer, primary_key=True, comment="外键 课程id")
    cname = db.Column(db.String(60), nullable=False)
    uid = db.Column(db.Integer, db.ForeignKey("accounts.aid"))
    price = db.Column(db.Float(10, 2), default=0.0)
    info = db.Column(db.Text)
    cimage = db.Column(db.String(250))
    create_at = db.Column(db.DateTime)
    delete_at = db.Column(db.DateTime)

    catalogs = db.relationship("Catalog",db.backref("curriculum"),db.lazyload("dynamic"))
    comments = db.relationship("CurriculumComments",db.backref("curriculum"),db.lazyload("dynamic"))


    def __repr__(self):
        return "数据库{}".format(self.__tablename__)