# coding=utf-8

from .RequestBaseForm import RequestBaseForm
from wtforms import StringField,PasswordField,IntegerField
from wtforms.validators import DataRequired,Length




# 添加收藏表单
class add_collection_form(RequestBaseForm):
    cid = IntegerField("cid",validators=[DataRequired()])
