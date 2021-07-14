# @Author  : Edlison
# @Date    : 7/12/21 17:23
from backend.api.user.model.user_model import User
from backend.api.user.model.user_relation import UserRelation
from backend.api import db
from sqlalchemy import and_
from hashlib import sha256


def get_user_by_name_password(user_name, user_password):
    """
    通过用户和密码获取用户

    Args:

    Returns:

    @Author  : Edlison
    @Date    : 1/4/21 17:00
    """
    user = User.query.filter(and_(User.user_name==user_name, User.user_password==user_password)).first()
    return user


def get_user_by_name(user_name):
    user = User.query.filter(User.user_name == user_name).first()
    return user


def get_user_by_id(user_id):
    user = User.query.filter_by(user_id=user_id).first()
    return user


def insert_user(user_name, user_password):
    user = User(user_name=user_name, user_password=sha256(user_password.encode('utf-8')).hexdigest())
    db.session.add(user)
    db.session.commit()


def get_relation_by_id(user_id, friend_id):
    relation = UserRelation.query.filter_by(user_id=user_id, friend_id=friend_id).first()
    return relation


def get_relations_all(user_id):
    relations = UserRelation.query.filter_by(user_id=user_id).all()
    return relations


def insert_user_relation(user_id, friend_id, room_id, friend_tag='default'):
    relation = UserRelation(user_id=user_id, friend_id=friend_id, room_id=room_id, friend_tag=friend_tag)
    db.session.add(relation)
    db.session.commit()


def update_friend_tag(user_id, friend_id, new_tag):
    relation = UserRelation.query.filter_by(user_id=user_id, friend_id=friend_id).first()
    relation.friend_tag = new_tag
    db.session.commit()


def get_room_by_id(user_id, friend_id):
    relation = UserRelation.query.filter_by(user_id=user_id, friend_id=friend_id).first()
    return relation


def delete_relation_by_id(user_id, friend_id):
    relation = UserRelation.query.filter_by(user_id=user_id, friend_id=friend_id).first()
    db.session.delete(relation)
    db.session.commit()
    return relation