# coding=utf-8

from .RequestBaseForm import RequestBaseForm
from wtforms import StringField
from wtforms.validators import DataRequired,Length

class Testform(RequestBaseForm):
    username = StringField("username",validators=[DataRequired(),Length(min=2,max=20)])
