# @Author  : Edlison
# @Date    : 7/12/21 18:47
from backend.api import db


class UserRelation(db.Model):
    __tablename__ = 'user_relation'
    user_id = db.Column(db.Integer, nullable=False, comment='主用户id', primary_key=True)
    friend_id = db.Column(db.Integer, nullable=False, comment='好友id', primary_key=True)
    friend_tag = db.Column(db.String(32), nullable=False, default='default', comment='好友分组')
    room_id = db.Column(db.String(64), nullable=False, comment='房间号')

    def __init__(self, user_id, friend_id, room_id, friend_tag='default'):
        self.user_id = user_id
        self.friend_id = friend_id
        self.friend_tag = friend_tag
        self.room_id = room_id

    def keys(self):
        return ['user_id', 'friend_id', 'friend_tag', 'room_id']

    def __getitem__(self, item):
        return getattr(self, item)

    def __repr__(self):
        return '<User {} and User {} in relation.>'.format(self.user_id, self.friend_id)


