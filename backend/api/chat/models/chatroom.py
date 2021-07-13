# @Author  : Edlison
# @Date    : 7/12/21 18:48
from backend.api import db


class Chatroom(db.Model):
    room_id = db.Column(db.Integer, nullable=False, comment='房间号', primary_key=True)
    room_log = db.Column(db.Text, nullable=True, comment='聊天记录')

    def __init__(self, room_id):
        self.room_id = room_id

    def keys(self):
        return ['room_id']

    def __getitem__(self, item):
        return getattr(self, item)

    def __repr__(self):
        return '<Room {}>'.format(self.room_id)
