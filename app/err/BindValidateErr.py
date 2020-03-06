#coding=utf-8

import json

def BindValidateErr(msg):
    res_item = {
        "code":30001,
        "msg" :msg,
        "data":None
    }
    return json.dumps(res_item)


