# coding=utf-8
from flask import Blueprint


user = Blueprint('user_api_v1',__name__)


# @user.before_request
# def wrapper():
#     print(request.path)
#     is_found = True
#     if is_found is False:
#         return jsonify("not found")
#     return None




# 登录
@user.route("login",methods=["POST"])
def login():
    return "login"

# 注册
@user.route("registry",methods=["POST"])
def registry():
    return ""

# 退出登录
@user.route("logout",methods=["POST"])
def logout():
    return ""



# 修改个人信息
@user.route("/modify/info",methods=["POST"])
def modify_user():
    return ""

# 修改密码
@user.route("/modify/password",methods=["POST"])
def modify_user_password():
    return ""

# 添加视频收藏
@user.route("/add/collection",methods=["POST"])
def add_collection():
    return ""


# 查看收藏视频
@user.route("/show/collection",methods=["GET"])
def show_collection():
    return ""


# 取消(删除)收藏
@user.route("/del/collection",methods=["DELETE","POST"])
def del_collection():
    return ""



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