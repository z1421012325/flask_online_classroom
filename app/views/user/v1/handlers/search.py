#coding=utf-8

from flask import Blueprint

search = Blueprint("search_api_v1",__name__)



# search 搜索  时间排序,购买排序
@search.route("/search",methods=["GET"])
def search_curriculum():
    return "{}".format(1)



