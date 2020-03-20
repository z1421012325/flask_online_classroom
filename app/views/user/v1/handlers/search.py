#coding=utf-8

from flask import Blueprint,jsonify,request

from OnlineClassroom.app.models.curriculums import Curriculums
from OnlineClassroom.app.forms.search_forms import *

from OnlineClassroom.app.serializetion.res_dict import *

search = Blueprint("search_api_v1",__name__)

# todo 还有排序没做  分页

# search 搜索  时间排序,购买排序
@search.route("/search",methods=["GET"])
def search_curriculum():

    key = request.args.get("key","")

    order = request.args.get("order", None)
    if order == None:
        order = False

    cc = Curriculums()
    items = cc.query_like_field_all(key)

    return jsonify(commen_success_res("",items))
