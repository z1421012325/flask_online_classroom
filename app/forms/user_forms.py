# coding=utf-8

from .RequestBaseForm import RequestBaseForm
from wtforms import StringField,PasswordField
from wtforms.validators import DataRequired,Length



# 注册表单
class registry_form(RequestBaseForm):
    nickname = StringField("nickname",validators=[DataRequired(),Length(min=2,max=20)])
    username = StringField("username",validators=[DataRequired(),Length(min=2,max=20)])
    pswd = PasswordField("pswd",validators=[DataRequired(),Length(min=8,max=50)])
    info = StringField("info")



# 登录表单
class login_form(RequestBaseForm):
    username = StringField("username",validators=[DataRequired(),Length(min=2,max=20)])
    pswd = PasswordField("pswd",validators=[DataRequired(),Length(min=8,max=50)])


# 修改账号信息
class modify_info_form(RequestBaseForm):
    nickname = StringField("nickname",validators=[DataRequired(),Length(min=2,max=20)])
    info = StringField("info")


# 修改账号密码
class modify_pswd_form(RequestBaseForm):
    old_pswd = PasswordField("old",validators=[DataRequired(),Length(min=8,max=50)])
    new_pswd = PasswordField("new", validators=[DataRequired(), Length(min=8, max=50)])