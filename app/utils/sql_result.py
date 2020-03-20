# coding=utf-8


import datetime


# 将sql原生语句执行之后返回的结果转换为字典格式
def sql_result_to_dict(results):
    list_items = []

    for result in results:
        item = {}
        for index ,key in enumerate(result.keys()):
            if isinstance(result[index], datetime.datetime) or isinstance(result[index], datetime.date):
                item[key] = result[index].strftime('%Y-%m-%d %H:%M:%S')
            else:
                item[key] = result[index]
        list_items.append(item)

    return list_items