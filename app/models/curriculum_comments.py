# coding=utf-8

import datetime
from OnlineClassroom.app.ext.plugins import db

from .account import *
#   UNIQUE KEY `ac_id` (`aid`,`cid`),
"""
课程评价
CREATE TABLE `curriculum_comments` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `cid` int DEFAULT NULL COMMENT '外键 课程id',
  `aid` int DEFAULT NULL COMMENT '外键 用户id',
  `number` tinyint(10) DEFAULT NULL COMMENT '评价分数',
  `comment` varchar(300) DEFAULT NULL COMMENT '评价',
  `create_at` datetime DEFAULT now() COMMENT '创建时间',
  `delete_at` datetime DEFAULT NULL COMMENT '删除时间',
  KEY `curriculum_comments_ibfk_1` (`aid`),
  KEY `curriculum_comments_ibfk_2` (`cid`),
  CONSTRAINT `curriculum_comments_ibfk_1` FOREIGN KEY (`aid`) REFERENCES `accounts` (`aid`),
  CONSTRAINT `curriculum_comments_ibfk_2` FOREIGN KEY (`cid`) REFERENCES `curriculums` (`cid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
"""
class CurriculumComments(db.Model):
    __tablename__ = "curriculum_comments"
    id = db.Column(db.Integer,primary_key=True,comment="主键")
    cid = db.Column(db.Integer, db.ForeignKey("curriculums.cid"),comment="外键 课程id") # primary_key=True
    aid = db.Column(db.Integer, db.ForeignKey("accounts.aid"),comment="外键 用户id") # primary_key=True
    number = db.Column(db.Integer,comment="评价分数")
    comment = db.Column(db.String(300), comment="评价")
    create_at = db.Column(db.DateTime,default=datetime.datetime.utcnow())
    delete_at = db.Column(db.DateTime)

    user = db.relationship(Account,backref="comments")

    def __repr__(self):
        return "数据库{}".format(self.__tablename__)

    def __init__(self,cid=None,aid=None,number=None,comment=None,id=None):
        self.cid = cid
        self.aid = aid
        self.number = number
        self.comment = comment
        self.id=id


    def get_comment_all(self):
        comments = self.query.filter_by(cid=self.cid,delete_at=None).all()

        items = {}
        list_item = []

        for comment in comments:
            item = comment.serializetion_item()
            list_item.append(item)

        items["datas"] = list_item
        items["len"] = len(comments)

        return items

    def serializetion_item(self):
        item = {
            "id":self.id,
            "aid":self.aid,
            "cid":self.cid,
            "name":self.user.nickname,
            "number": self.number,
            "comment": self.comment,
            "create_at": self.create_at,
        }
        return item


    def is_commit(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except Exception as e:
            db.rollback()
            return False


    def save(self):
        if self.number == None:
            self.number = 0
        self.create_at = datetime.datetime.utcnow()
        return self.is_commit()


    def query_user_comments(self):
        comments = self.query.filter_by(aid=self.aid).all()

        items = {}
        list_item = []

        for comment in comments:
            list_item.append(comment.serializetion_item())

        items["datas"] = list_item
        items["len"] = len(comments)

        return items

    def del_comment(self):
        comment = self.query.filter_by(id=self.id).first()
        comment.delete_at = datetime.datetime.utcnow()

        return self.is_commit()