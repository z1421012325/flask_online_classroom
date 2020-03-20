# coding=utf-8

from .RequestBaseForm import RequestBaseForm
from wtforms import StringField,PasswordField,IntegerField,FloatField
from wtforms.validators import DataRequired,Length




class search_form(RequestBaseForm):
    key = StringField("key",validators=[DataRequired])
    order = IntegerField("order",validators=[])



