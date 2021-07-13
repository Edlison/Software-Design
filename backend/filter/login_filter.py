# @Author  : Edlison
# @Date    : 7/12/21 17:18
from functools import wraps
from flask import session, jsonify, g
from backend.result.system_result import SystemResult


def need_login(f):
    @wraps(f)  # 保留被装饰函数的属性
    def inner(*args, **kwargs):
        # 查看session
        user_name = session.get('user_name')
        if user_name:  # 获取到了session 继续执行原函数
            g.user_name = user_name
            return f(*args, **kwargs)
        else:  # 没有session 直接返回失败的json
            res = SystemResult().error('未登陆')
            return jsonify(dict(res))
    return inner
