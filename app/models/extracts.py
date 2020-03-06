# coding=utf-8

from OnlineClassroom.app.ext.plugins import db

"""
金额提取
CREATE TABLE `extracts` (
  `eid` int NOT NULL AUTO_INCREMENT COMMENT '主键自增长',
  `create_at` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `t_money` float(10,2) DEFAULT NULL COMMENT '提取金额',
  `divide` float(10,2) DEFAULT 0.05 COMMENT '站点分成,默认为5%',
  `actual_money` float(10,2) DEFAULT NULL COMMENT '实际提成',
  `aid` int DEFAULT NULL COMMENT '外键 用户id',
  `number` varchar(35) DEFAULT NULL COMMENT '流水号',
  PRIMARY KEY (`eid`),
  KEY `aid` (`aid`),
  CONSTRAINT `extracts_ibfk_1` FOREIGN KEY (`aid`) REFERENCES `accounts` (`aid`)
) ENGINE=InnoDB AUTO_INCREMENT=100000 DEFAULT CHARSET=utf8
"""
class Extracts(db.Model):
    __tablename__ = "extracts"
    eid = db.Column(db.Integer, primary_key=True, comment="外键 课程id")
    create_at = db.Column(db.DateTime, comment="创建时间")
    t_money = db.Column(db.Float(10,2), comment="提取金额")
    divide = db.Column(db.Float(10, 2),default=0.05, comment="站点分成,默认为5%")
    actual_money = db.Column(db.Float(10, 2), comment="实际提成")
    aid = db.Column(db.Integer, db.ForeignKey("accounts.aid"),comment="外键 用户id")
    number = db.Column(db.String(35),  comment="流水号")


    def __repr__(self):
        return "数据库{}".format(self.__tablename__)