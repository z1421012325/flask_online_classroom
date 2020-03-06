# coding=utf-8
from OnlineClassroom.app.ext.plugins import db

"""
用户收藏课程
CREATE TABLE `use_collections` (
  `aid` int DEFAULT NULL COMMENT '外键 用户id',
  `cid` int DEFAULT NULL COMMENT '外键 课程id',
  KEY `cid` (`cid`),
  KEY `aid` (`aid`),
  CONSTRAINT `use_collections_ibfk_1` FOREIGN KEY (`cid`) REFERENCES `curriculums` (`cid`),
  CONSTRAINT `use_collections_ibfk_2` FOREIGN KEY (`aid`) REFERENCES `accounts` (`aid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
"""


class UseCollections(db.Model):
    __tablename__ = "use_collections"
    aid = db.Column(db.Integer, db.ForeignKey("accounts.aid"),comment="外键 课程id")
    cid = db.Column(db.Integer, db.ForeignKey("curriculums.cid"),comment="外键 课程id")

    curriculums = db.relationship("Curriculums", db.backref("use_collections"), db.lazyload("dynamic"))

    def __repr__(self):
        return "数据库{}".format(self.__tablename__)