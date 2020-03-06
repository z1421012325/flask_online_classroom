# coding=utf-8


from OnlineClassroom.app.ext.plugins import db

"""
课程评价
CREATE TABLE `curriculum_comments` (
  `cid` int DEFAULT NULL COMMENT '外键 课程id',
  `uid` int DEFAULT NULL COMMENT '外键 用户id',
  `number` tinyint(10) DEFAULT NULL COMMENT '评价分数',
  `comment` varchar(300) DEFAULT NULL COMMENT '评价',
  `create_at` datetime DEFAULT now() COMMENT '创建时间',
  `delete_at` datetime DEFAULT NULL COMMENT '删除时间',
  UNIQUE KEY `u_id` (`uid`,`cid`),
  KEY `curriculum_comments_ibfk_2` (`cid`),
  CONSTRAINT `curriculum_comments_ibfk_1` FOREIGN KEY (`uid`) REFERENCES `accounts` (`aid`),
  CONSTRAINT `curriculum_comments_ibfk_2` FOREIGN KEY (`cid`) REFERENCES `curriculums` (`cid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
"""
class CurriculumComments(db.Model):
    __tablename__ = "curriculum_comments"
    cid = db.Column(db.Integer, db.ForeignKey("curriculums.cid"),comment="外键 课程id")
    uid = db.Column(db.Integer, db.ForeignKey("accounts.aid"),comment="外键 用户id")
    number = db.Column(db.Integer,comment="评价分数")
    comment = db.Column(db.String(300), comment="评价")
    create_at = db.Column(db.DateTime)
    delete_at = db.Column(db.DateTime)

    def __repr__(self):
        return "数据库{}".format(self.__tablename__)