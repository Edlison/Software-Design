# @Author  : Edlison
# @Date    : 7/12/21 17:23
from flask import g
from backend.result.system_result import SystemResult
from backend.api.user.mapper.user_mapper import get_user_by_name_password, get_user_by_name, insert_user, \
    insert_user_relation, get_relation_by_id, update_friend_tag, get_relations_all, get_user_by_id, get_room_by_id
from backend.util.serialize import serialize_model_list
from hashlib import sha256
from uuid import uuid4


def register(user_name, user_password):
    user = get_user_by_name(user_name)
    res = SystemResult()
    if user:
        return res.error('user has existed.')
    else:
        insert_user(user_name, user_password)
        return res.ok('insert user success.')


def validate(user_name, user_password):
    """
    密码验证逻辑

    Args:

    Returns:

    @Author  : Edlison
    @Date    : 1/4/21 16:59
    """
    user = get_user_by_name_password(user_name, sha256(user_password.encode('utf-8')).hexdigest())
    if user:
        g.user_id = user.user_id
        res = SystemResult().ok()
    else:
        res = SystemResult().error()
    return res


def get_info(user_id):
    user = get_user_by_id(user_id)
    res = SystemResult()
    res.ok('get info success.')
    res.set_data({'user_name': user.user_name})
    return res


def get_friends_all(user_id):
    res = SystemResult()
    relations = get_relations_all(user_id)
    res.ok('get success.')
    res.set_data(serialize_model_list(relations))
    return res


def get_friend_room(user_id, friend_id):
    relation = get_room_by_id(user_id, friend_id)
    res = SystemResult()
    if relation:
        res.ok('get room id success.')
        res.set_data({'room_id': relation['room_id']})
        return res
    else:
        res.error('get room id fail.')
        return res


def add_friend(user_id, friend_id):
    res = SystemResult()
    user = get_user_by_id(friend_id)
    if not in_relation(user_id, friend_id) and user:
        room_id = str(uuid4())
        insert_user_relation(user_id, friend_id, room_id=room_id)
        insert_user_relation(friend_id, user_id, room_id=room_id)
        return res.ok('add friend success.')
    else:
        return res.error('friend has existed or do not have this user.')


def update_tag(user_id, friend_id, new_tag):
    res = SystemResult()
    if in_relation(user_id, friend_id):
        update_friend_tag(user_id, friend_id, new_tag)
        return res.ok('update tag success.')
    else:
        return res.error('not friend.')


def in_relation(user_id, friend_id):
    relation1 = get_relation_by_id(user_id, friend_id)
    relation2 = get_relation_by_id(friend_id, user_id)
    return relation1 and relation2

