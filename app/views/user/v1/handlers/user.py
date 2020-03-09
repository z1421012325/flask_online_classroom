# coding=utf-8

from flask import Blueprint,jsonify,request
from OnlineClassroom.app.forms.user_forms import *
from OnlineClassroom.app.models.account import Account as account
from OnlineClassroom.app.ext.plugins import db
from OnlineClassroom.app.serialzietion.res_dict import *
from OnlineClassroom.app.utils.get_token import check_token,create_token,requst_get_token

user = Blueprint('user_api_v1',__name__)



# 登录
@user.route("login",methods=["POST"])
def login():

    form = login_form()
    if not form.validate_for_api():
        return jsonify(form.bindErr)

    u = account.query.filter(account.username==form.username.data).first()
    if not u.CheckPassword(form.pswd.data):
        return jsonify(pawd_check_err(""))

    # todo 返回token 塞入数据为用户id
    token = create_token(u.aid)

    item = {
        "username":u.username,
        "nickname":u.nickname,
        "token":token
    }

    return jsonify(commen_success_res("",item))



# 注册
@user.route("registry",methods=["POST"])
def registry():

    form = registry_form()
    if not form.validate_for_api():
        return jsonify(form.bindErr)

    u = account(form.nickname.data,form.username.data,form.pswd.data,form.info.data)

    if not u.registryAccount():
        return jsonify(registry_account_existence_res(""))

    return jsonify(registry_success_res())



# 退出登录
@user.route("logout",methods=["POST"])
def logout():
    token = requst_get_token()
    print(token)
    return jsonify(commen_success_res("",""))


# 修改个人信息 (昵称,info)
@user.route("/modify/info",methods=["POST"])
def modify_user():

    form = modify_info_form()
    if not form.validate_for_api():
        return jsonify(form.bindErr)


    token = requst_get_token()
    ok,aid = check_token(token)
    if not ok:
        return jsonify(token_err(""))

    u = account.query.filter(account.aid==int(aid)).first()
    if not u.modify_user_info(form.nickname.data,form.info.data):
        return jsonify(modify_err(""))

    return jsonify(commen_success_res("修改信息成功",""))







# 修改密码
@user.route("/modify/password",methods=["POST"])
def modify_user_password():

    form = modify_pswd_form()
    if not form.validate_for_api():
        return jsonify(form.bindErr)

    token = requst_get_token()
    ok, aid = check_token(token)
    if not ok:
        return jsonify(token_err(""))

    u = account.query.filter(account.aid == int(aid)).first()

    if not u.modify_pswd(form.old.data,form.new.data):
        return jsonify(modify_err(""))

    return jsonify(commen_success_res("密码修改成功",""))












# 用户信息
@user.route("/info/<int:uid>",methods=["GET"])
def get_user_info(uid):
    return "{}".format(uid)


# 查看学习的视频
@user.route("/show/study",methods=["GET"])
def get_show_study():
    return "{}".format(1)



# 发表评论
@user.route("/add/comment",methods=["POST"])
def add_comment():
    return "{}".format(1)

# 查看评论
@user.route("/see/comment",methods=["GET"])
def see_comment():
    return "{}".format(1)


# 删除评论
@user.route("/del/comment",methods=["DELETE"])
def del_comment():
    return "{}".format(1)



# 给予aliyun-oss凭证 让前端去aliyun-oss上传
@user.route("/get/oss/token",methods=["POST"])
def get_oss_token():
    return "{}".format(1)

# 保存用户头像
@user.route("/save/portrait",methods=["POST"])
def save_portrait():
    return "{}".format(1)


# 查看购物车
@user.route("/show/shopping",methods=["GET"])
def show_shopping():
    return "{}".format(1)








# 购物车下单状态更改(购买) 添加订单
@user.route("/modify/shopping/status",methods=["POST"])
def modify_shopping_status():
    return "{}".format(1)


# 查看课程购买记录(学生or老师)
@user.route("/show/curriculum/record",methods=["GET"])
def show_curriculum_record():
    return "{}".format(1)


# 查看课程被购买记录(老师) 含价格为0的课程
@user.route("/show/teacher/curriculum/record",methods=["GET"])
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