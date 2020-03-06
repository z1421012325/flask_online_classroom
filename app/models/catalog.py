# coding=utf-8

from OnlineClassroom.app.ext.plugins import db
# from OnlineClassroom.app.models.account import Account

"""
课程目录
 CREATE TABLE `catalog` (
  `cat_id` int DEFAULT NULL COMMENT '外键 课程id',
  `name` varchar(50) DEFAULT NULL COMMENT '课程目录名称',
  `url` varchar(255) DEFAULT NULL COMMENT '目录地址',
  `create_at` datetime DEFAULT now() COMMENT '一个课程多个目录,根据时间排序',
  `delete_at` datetime DEFAULT null COMMENT '删除时间,软删除',
  KEY `cat_id` (`cat_id`),
  CONSTRAINT `catalog_ibfk_1` FOREIGN KEY (`cat_id`) REFERENCES `curriculums` (`cid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8
"""


class Catalog(db.Model):
    __tablename__ = "catalog"

    cat_id = db.Column(db.Integer,db.ForeignKey("curriculums.cid"), primary_key=True,comment="外键 课程id")
    name = db.Column(db.String(50),nullable=False,comment="课程目录名称")
    url = db.Column(db.String(255),nullable=False,comment="目录地址")
    create_at = db.Column(db.DateTime,comment="一个课程多个目录,根据时间排序")
    delete_at = db.Column(db.DateTime,comment="删除时间,软删除")

    def __repr__(self):
        return "数据库{}".format(self.__tablename__)