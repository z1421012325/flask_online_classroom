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


class use_collections(db.Model):
    __tablename__ = "use_collections"
    aid = db.Column(db.Integer,db.ForeignKey("accounts.aid"),primary_key=True, comment="外键 用户id")
    cid = db.Column(db.Integer, db.ForeignKey("curriculums.cid"),primary_key=True, comment="外键 课程id")

    curriculums = db.relationship("Curriculums", backref="use_collections")


    def __repr__(self):
        return "数据库{}".format(self.__tablename__)

    def __init__(self,aid,cid):
        self.aid = aid
        self.cid = cid



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

    def query_use_curriculms(self):

        datas = {}
        list_items = []

        for dict_item in self.curriculum:
            list_items.append(dict_item)

        print(list_items)
        datas["data"] = list_items

        # 查询个数和总个数
        total = 0
        datas["total"] = total
        current_number = 0
        datas["current_number"] = current_number

        return datas