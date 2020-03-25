# coding=utf-8

from flask import Blueprint,jsonify

from OnlineClassroom.app.forms.admin_forms import *
from OnlineClassroom.app.forms.paginate_form import *
from OnlineClassroom.app.serializetion.res_dict import *

from OnlineClassroom.app.models.admin_user import *
from OnlineClassroom.app.models.admin_role import *
from OnlineClassroom.app.models.curriculums import *
from OnlineClassroom.app.models.account import *

from OnlineClassroom.app.utils.get_token import *

admin = Blueprint('admin_api_v1',__name__)

# 注册, todo
@admin.route("/registry")
def registry():

    form = registry_form()
    if not form.validate_for_api():
        return form.bindErr

    u = Admin_Users(username=form.username.data,pswd=form.pswd.data,aid=form.aid.data)
    if not u.save():
        return jsonify(add_err(""))

    return jsonify(registry_success_res())

# 登录
@admin.route("/login")
def login():

    form = login_form()
    if not form.validate_for_api():
        return form.bindErr

    u = Admin_Users(username=form.username.data)
    _u,ok = u.check_login_user_pswd(form.pswd.data)
    if not ok:
        return jsonify(pswd_check_err(""))

    token = create_admin_token(u.get_aid(),u.get_username(),u.get_rid())
    dict_res = {
        "code":10000,
        "msg":"success",
        "data":token
    }

    return jsonify(dict_res)

# 退出
@admin.route("/logout")
def logout():
    token = requst_get_token()
    ok, data = check_admin_token(token)
    return jsonify(commen_success_res("logout out ",data))


# 拥有管理权限人员对普通员工账号激活,只能激活下一级,平级无法激活
@admin.route("")
def activation_user():

    form = activation_user_status_form()
    if not form.validate_for_api():
        return form.bindErr

    token = requst_get_token()
    ok, data = check_admin_token(token)
    if not ok:
        return jsonify(token_err(""))

    u1 = Admin_Users(aid=data.get("aid"))
    up_u1 = u1.get_user_aid_activation()

    u2 = Admin_Users(aid=form.aid.data)
    _u2 = u2.get_user_aid_unactivation()

    if up_u1.status <= _u2.status:
        return jsonify(modify_err("权限等级过低,无法激活"))

    if not _u2.modift_auth_status(form.grade.data):
        return jsonify(modify_err("账号状态异常"))

    return jsonify(commen_success_res("权限修改成功",""))


# 员工修改本身账号密码
@admin.route("")
def modify_is_pswd():

    form = modify_pswd_form()
    if not form.validate_for_api():
        return form.bindErr

    token = requst_get_token()
    ok, data = check_admin_token(token)
    if not ok:
        return jsonify(token_err(""))

    u = Admin_Users(aid=data.get("aid"), username=data.get("username"))
    _u,ok = u.check_login_user_pswd(form.old.data)
    if not ok :
        return jsonify(modify_err("账号或者密码错误"))

    if not _u.modify_pswd(form.new.data):
        return jsonify(modify_err("修改密码错误"))

    return jsonify(commen_success_res("修改密码成功",""))

# 修改下级员工权限
@admin.route("")
def modify_is_pswd():
    form = modify_user_status_form()
    if not form.validate_for_api():
        return form.bindErr

    token = requst_get_token()
    ok, data = check_admin_token(token)
    if not ok:
        return jsonify(token_err(""))

    u1 = Admin_Users(aid=data.get("aid"))
    up_u1 = u1.get_user_aid_activation()

    u2 = Admin_Users(aid=form.aid.data)
    _u2 = u2.get_user_aid_activation()

    if up_u1.status <= _u2.status:
        return jsonify(modify_err("权限等级过低,无法修改"))

    if not _u2.modift_auth_status(form.grade.data):
        return jsonify(modify_err("账号状态修改异常"))

    return jsonify(commen_success_res("修改权限成功", ""))




# 查看未激活员工账号
@admin.route("")
def show_user_unstatus():

    form = page_form()

    u = Admin_Users()
    items = u.get_unactivation_accounts(page=form.page.data,number=form.number.data)

    return  jsonify(commen_success_res("",items))


# 查看离职员工账号
@admin.route("")
def show_user_leave():

    form = page_form()

    u = Admin_Users()
    items = u.get_leave_accounts(page=form.page.data, number=form.number.data)

    return jsonify(commen_success_res("", items))


# 查看所有员工账号
@admin.route("")
def show_user_all():

    form = page_form()

    u = Admin_Users()
    items = u.get_all_accounts(page=form.page.data, number=form.number.data)

    return jsonify(commen_success_res("", items))



# 查看视频和总个数
@admin.route("")
def show_video_total():
    form = page_form()

    c = Curriculums()
    items = c.query_curriculums_is_not_del()
    return jsonify(commen_success_res("", items))


# 查看一定天数之内的视频总数
@admin.route("")
def show_curriculum_total_day():
    form = show_curriculum_count_day_form()

    c = Curriculums()
    items = c.get_arbitrarily_curriculum_count(day=form.day.data)
    return jsonify(commen_success_res("", items))

# 查看一定天数之内被删的视频总数
@admin.route("")
def show_curriculum_is_del_total_day():
    form = show_curriculum_count_day_form()

    c = Curriculums()
    items = c.get_arbitrarily_curriculum_is_del_count(day=form.day.data)
    return jsonify(commen_success_res("", items))


# 根据天数查看当天视频上传个数
@admin.route("")
def show_curriculum_count_day():

    form = show_up_curriculum_count_form()

    c = Curriculums()
    items = c.get_day_up_curriculums_count(form.day.data)
    return jsonify(commen_success_res("", items))




# 根据天数查看正常注册的人数
@admin.route("")
def show_user_count_day():
    form = show_up_curriculum_count_form()

    u = Account()
    items = u.get_day_registry_count(form.day.data)
    return jsonify(commen_success_res("", items))


# 查看总注册人数
@admin.route("")
def show_user_total():
    u = Account()

    items = u.get_registry_counts()
    return jsonify(commen_success_res("", items))


# 查看用户列表
@admin.route("")
def show_users_list():
    form = page_form()

    u = Account()
    items = u.get_users(page=form.page.data,number=form.number.data)

    return jsonify(commen_success_res("", items))

# 封禁用户
@admin.route("")
def del_prohibit_user():

    form = del_prohibit_user_form()
    if not form.validate_for_api():
        return form.bindErr

    token = requst_get_token()
    ok, data = check_admin_token(token)
    if not ok:
        return jsonify(token_err(""))

    u = Account(aid=form.aid.data)
    if not u.prohibit_user(int(data.get("aid"))):
        return jsonify(modify_err(""))

    return jsonify(commen_success_res("封禁用户成功",""))



# 查看封禁用户
@admin.route("")
def show_prohibit_users():

    form = page_form()

    u = Account()
    items = u.get_prohibit_users(page=form.page.data,number=form.number.data)

    return jsonify(commen_success_res("",items))


# 解封用户
@admin.route("")
def adopt_user():

    token = requst_get_token()
    ok, data = check_admin_token(token)
    if not ok:
        return jsonify(token_err(""))

    form = adopt_user_form()
    if not form.validate_for_api():
        return form.bindErr

    u = Account(aid=form.aid.data)
    if not u.reduction_prohibit_user(admin_aid=data.get("aid")):
        return jsonify(modify_err("解封用户异常"))

    return jsonify(commen_success_res("解封用户成功",""))



# 查看视频
@admin.route("")
def show_list_video():



    pass

# 下架视频
@admin.route("")
def del_video():
    pass

# 恢复视频
@admin.route("")
def adopt_video():
    pass


# 查看评论
@admin.route("")
def show_comments():
    pass
# 删除评论
@admin.route("")
def del_comment():
    pass

# 恢复评论
@admin.route("")
def adopt_comment():
    pass

# 根据天数查看当天下单金额
@admin.route("")
def show_day_money_day():
    pass

# 根据月份查看当月下单金额
@admin.route("")
def show_month_money_month():
    pass

# 总共下单金额
@admin.route("")
def show_total_money():
    pass

# 站点提成金额总数
@admin.route("")
def show_site_royalty_money():
    pass

# 根据天数查看当天提成金额
@admin.route("")
def show_site_royalty_money_day():
    pass

# 被老师提取出去的金额总数
@admin.route("")
def show_teacher_royalty_money():
    pass

# 根据天数查看被老师提取出去的金额总数F
@admin.route("")
def show_teacher_royalty_money_day():
    pass

