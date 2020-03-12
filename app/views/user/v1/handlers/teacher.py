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



# 查看课程被购买记录(老师) 含价格为0的课程
@teacher.route("/show/curriculum/record",methods=["GET"])
def show_teacher_curriculum_record():
    return "{}".format(1)


# 查看拥有金额(老师)
@user.route("/have/money",methods=["GET"])
def have_money():
    return "{}".format(1)


# 提成金额(老师)  zfb
@user.route("/extract/money",methods=["GET"])
def extract_money():
    return "{}".format(1)


# 提成记录(老师)
@user.route("/extract/record",methods=["GET"])
def extract_record():
    return "{}".format(1)