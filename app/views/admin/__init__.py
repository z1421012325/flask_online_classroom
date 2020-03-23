# coding=utf-8
from flask import Blueprint


admin = Blueprint('admin_api_v1',__name__)

# 注册, todo 新建员工表和权限表
@admin.route("registry")
def registry():
    return "nihao "

# 登录
@admin.route("")
def login():
    pass


# 退出
@admin.route("")
def logout():
    pass

# 查看视频和总个数
@admin.route("")
def show_video_total():
    pass

# 根据天数查看当天视频上传个数 使用参数控制返回数据范围 1 - 365
@admin.route("")
def show_curriculum_count_day():
    pass


# 根据天数查看正常注册的人数(学生or老师or全部)
@admin.route("")
def show_user_count_day():
    pass


# 查看总注册人数(老师or学生or全部)
@admin.route("")
def show_user_total():
    pass

# 查看用户列表
@admin.route("")
def show_users_list():
    pass



# 封禁用户 todo 使用用户中的status字段
@admin.route("")
def del_prohibit_user():
    pass

# 查看封禁用户
@admin.route("")
def show_prohibit_users():
    pass


# 解封用户
@admin.route("")
def adopt_user():
    pass


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

