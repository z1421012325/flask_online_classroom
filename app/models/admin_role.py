# coding=utf-8


# 员工权限表
"""
角色
CREATE TABLE `admin_roles` (
  `r_id` int NOT NULL COMMENT '角色id,表示员工权限,1普通员工,2组长?,3主管,9老板-- 123都有增删改查权限.3能注册12权限员工,9(我全都要)',
  `r_name` char(10) DEFAULT '普通员工' COMMENT '角色名字'
) ENGINE=InnoDB DEFAULT CHARSET=utf8

insert into admin_roles (r_id,r_name) values (1,'普通员工')
insert into admin_roles (r_id,r_name) values (2,'组长')
insert into admin_roles (r_id,r_name) values (3,'主管')
insert into admin_roles (r_id,r_name) values (9,'boss')
"""