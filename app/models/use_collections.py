# coding=utf-8

import datetime
from OnlineClassroom.app.ext.plugins import db

"""
用户收藏课程
CREATE TABLE `use_collections` (
  `aid` int DEFAULT NULL COMMENT '外键 用户id',
  `cid` int DEFAULT NULL COMMENT '外键 课程id',
  `create_at` datetime DEFAULT now() COMMENT '创建时间',
  `delete_at` datetime DEFAULT null COMMENT '删除时间,软删除',
  KEY `cid` (`cid`),
  KEY `aid` (`aid`),
  CONSTRAINT `use_collections_ibfk_1` FOREIGN KEY (`cid`) REFERENCES `curriculums` (`cid`),
  CONSTRAINT `use_collections_ibfk_2` FOREIGN KEY (`aid`) REFERENCES `accounts` (`aid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
"""


class use_collections(db.Model):
    __tablename__ = "use_collections"
    aid = db.Column(db.Integer,db.ForeignKey("accounts.aid"),primary_key=True, comment="外键 用户id")
    cid = db.Column(db.Integer, db.ForeignKey("curriculums.cid"),primary_key=True, comment="外键 课程id")
    create_at = db.Column(db.DateTime, default=datetime.datetime.utcnow(), comment="一个课程多个目录,根据时间排序")
    delete_at = db.Column(db.DateTime, comment="删除时间,软删除")

    curriculums = db.relationship("Curriculums", backref="use_collections")


    def __repr__(self):
        return "数据库{}".format(self.__tablename__)

    def __init__(self,aid=None,cid=None):
        self.aid = aid
        self.cid = cid
        self.create_at = datetime.datetime.utcnow()



    def add_use_collection(self):
        return self.is_commit()


    def is_commit(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except Exception as e:
            db.rollback()
            return False


    # 查询收藏课程
    # todo 测试一下
    def query_use_curriculms(self):

        datas = {}
        list_items = []

        for cc in self.curriculum:
            print(type(cc))     # 看是否为课程类class  如果是则进行一个字典化
            print(cc)
            list_items.append(cc)

        print(list_items)
        datas["data"] = list_items

        # 查询个数和总个数
        total = 0
        datas["total"] = total
        current_number = 0
        datas["current_number"] = current_number

        return datas




    def del_collection(self):
        self.delete_at = datetime.datetime.utcnow()
        return self.is_commit()
