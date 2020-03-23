# coding=utf-8


# 内部员工表
"""
create table admins_user (
`aid` int primary key auto_increment comment '内部员工id',
`username` char(20) not null comment '账号',
`pswd` varchar(255) not null comment '密码',
`status` tinyint default '0' comment '身份状态 0为未激活,1激活成功可使用,9离职(其他)',
`create_at` datetime default now())
ENGINE=InnoDB AUTO_INCREMENT=10000 DEFAULT CHARSET=utf8;
"""

