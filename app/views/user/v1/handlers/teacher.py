#coding=utf-8

from flask import Blueprint

teacher = Blueprint("teacher_api_v1",__name__)





# 老师注册
@teacher.route("registry",methods=["POST"])
def registry():
    return ""



# 展示所含有的老师
@teacher.route("/all",methods=["GET"])
def teacher_all():
    return "teacher"
