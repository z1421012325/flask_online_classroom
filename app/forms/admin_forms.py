from .RequestBaseForm import RequestBaseForm
from wtforms import StringField,PasswordField,IntegerField
from wtforms.validators import DataRequired,Length



# 注册表单
class registry_form(RequestBaseForm):
    username = StringField("username",validators=[DataRequired(),Length(min=2,max=20)])
    pswd = PasswordField("pswd",validators=[DataRequired(),Length(min=8,max=50)])
    aid = IntegerField("aid", validators=[])


# 登录表单
class login_form(RequestBaseForm):
    username = StringField("username",validators=[DataRequired(),Length(min=2,max=20)])
    pswd = PasswordField("pswd",validators=[DataRequired(),Length(min=8,max=50)])


# 修改账号信息
class modify_pswd_form(RequestBaseForm):
    old = StringField("old", validators=[DataRequired(), Length(min=8, max=50)])
    new = StringField("new", validators=[DataRequired(), Length(min=8, max=50)])


# 激活员工账号
class activation_user_status_form(RequestBaseForm):
    aid = IntegerField("aid", validators=[DataRequired()])
    grade = IntegerField("grade", validators=[DataRequired()])



# 修改员工账号
class modify_user_status_form(RequestBaseForm):
    aid = IntegerField("aid", validators=[DataRequired()])
    grade = IntegerField("grade", validators=[DataRequired()])


# 根据天数查看当天视频上传个数 使用参数控制返回数据范围 1 - 365
class show_curriculum_count_day_form(RequestBaseForm):
    day = IntegerField("day", validators=[])


# 每天上传总数
class show_up_curriculum_count_form(RequestBaseForm):
    day = IntegerField("day", validators=[])


# 封禁用户
class del_prohibit_user_form(RequestBaseForm):
    aid = IntegerField("aid", validators=[DataRequired()])

# 解封用户
class adopt_user_form(RequestBaseForm):
    aid = IntegerField("aid", validators=[DataRequired()])

# 下架视频
class admin_del_video_form(RequestBaseForm):
    cid = IntegerField("cid", validators=[DataRequired()])


# 恢复视频
class admin_recovery_video_form(RequestBaseForm):
    cid = IntegerField("cid", validators=[DataRequired()])

# 删除评论
class admin_del_comment_form(RequestBaseForm):
    id = IntegerField("id", validators=[DataRequired()])

# 恢复评论
class admin_recovery_comment_form(RequestBaseForm):
    id = IntegerField("id", validators=[DataRequired()])