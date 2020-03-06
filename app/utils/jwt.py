#coding=utf-8


import time
import jwt
from OnlineClassroom.app import create_app


exp_time = 86400 * 30                       # 过期时间
algorithm = "RS256"                         # 算法
SECRET_KEY = ""                             # 盐值
DEFAULT_SECRET_KEY =  "12345679"            # 默认盐值


def get_secret_key():
    secret_key = create_app().config.get('SECRET_KEY')
    if len(secret_key) == 0:
        secret_key = DEFAULT_SECRET_KEY
    return secret_key


def create_jwt_token(data):

    SECRET_KEY = get_secret_key()

    payload = {
        "iat":time.time(),
        "exp":int(time.time()) + exp_time,
        "uid":1,
        "data":data
    }


    token = jwt.encode(payload, SECRET_KEY, algorithm=algorithm)
    print(token)


def Check_jwt_token(token):

    payload = jwt.decode(token, 'secret', algorithms=[algorithm])
    if payload:
        return True, payload
    return False, payload


if __name__ == '__main__':
    create_jwt_token()


