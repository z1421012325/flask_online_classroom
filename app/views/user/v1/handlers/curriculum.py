#coding=utf-8

from flask import Blueprint,jsonify,request
from OnlineClassroom.app.forms.curriculum_forms import *
from OnlineClassroom.app.models.use_collections import *
from OnlineClassroom.app.models.account import *
from OnlineClassroom.app.models.use_collections import *
from OnlineClassroom.app.serialzietion.res_dict import *
from OnlineClassroom.app.utils.get_token import *

curriculum = Blueprint("curriculum_api_v1",__name__)




# 添加视频收藏
@curriculum.route("/add/collection",methods=["POST"])
def add_collection():

    form = add_collection_form()
    if not form.validate_for_api():
        return form.BindErrToRes("")

    token = requst_get_token()
    ok, aid = check_token(token)
    if not ok:
        return jsonify(token_err(""))

    uc = use_collections(int(aid),form.cid.data)
    if not uc.add_use_collection():
        return jsonify(add_err("课程收藏异常"))

    return jsonify(commen_success_res("课程收藏成功",""))


# 查看收藏视频
@curriculum.route("/show/collection",methods=["GET"])
def show_collection():

    token = requst_get_token()
    ok, aid = check_token(token)
    if not ok:
        return jsonify(token_err(""))

    uc = use_collections.query.filter_by(aid=int(aid)).first()
    # uc.query_use_curriculms()

    print("route >> :",uc)

    return ""











# 取消(删除)收藏
@curriculum.route("/del/collection",methods=["DELETE","POST"])
def del_collection():
    return ""













# 课程页面
@curriculum.route("/course/<int:cid>",methods=["GET"])
def course_curriculum(cid):
    return "{}".format(cid)


# 课程目录
@curriculum.route("/course/coursedetail/<int:cid>",methods=["GET"])
def course_coursedetail_curriculum(cid):
    return "{}".format(cid)


# 课程评论
@curriculum.route("/comment/<int:cid>",methods=["GET"])
def course_comment(cid):
    return "{}".format(cid)



# 课程目录
@curriculum.route("/catalog/<int:cid>",methods=["GET"])
def curriculum_catalog(cid):
    return "{}".format(cid)



# 开始学习,要对是否登录用户检测,或者课程价格为0or不为0检测(是否购买检测)
@curriculum.route("/check/<int:cid>",methods=["GET"])
def curriculum_check(cid):
    return "{}".format(cid)



# 课程推荐(老师本人还是根据标签推荐有前端决定,后端输出 degree)
@curriculum.route("/recommend/<int:cid>",methods=["GET"])
def curriculum_recommend(cid):
    return "{}".format(cid)



# 该老师其他教学课程
@curriculum.route("/other",methods=["GET"])
def curriculum_other():
    return "{}".format()




# 给予aliyun-oss凭证 让前端去aliyun-oss上传
@curriculum.route("/get/oss/token",methods=["POST"])
def get_oss_token():
    return "{}".format(1)


# 新增视频 保存上传视频(老师)url
@curriculum.route("/save/new/video",methods=["POST"])
def save_new_video():
    return "{}".format(1)




# 查看视频信息(老师)
@curriculum.route("/see/<int:cid>",methods=["GET"])
def curriculum_see(cid):
    return "{}".format(cid)



# 修改视频目录信息(老师)
@curriculum.route("/modify/video/catalog",methods=["POST"])
def modify_video_catalog():
    return "{}".format(1)



#  删除视频目录信息(老师)
@curriculum.route("/del/video/catalog",methods=["POST","DELETE"])
def del_video_catalog():
    return "{}".format(1)


#  添加课程的视频目录(老师)
@curriculum.route("/add/video/catalog",methods=["POST"])
def add_video_catalog():
    return "{}".format(1)



# 下架视频
@curriculum.route("/del/video",methods=["DELETE"])
def del_video():
    return "{}".format(1)

# 查看下架的视频
@curriculum.route("/show/video",methods=["GET"])
def show_video():
    return "{}".format(1)


# 恢复下架视频(老师)
@curriculum.route("/recovery/video",methods=["POST"])
def recovery_video():
    return "{}".format(1)


# 添加购物车,不是直接订单
@curriculum.route("/add/shopping",methods=["POST"])
def add_shopping():
    return "{}".format(1)