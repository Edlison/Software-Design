# @Author  : Edlison
# @Date    : 7/12/21 17:05
from backend.api import db


class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='用户ID')
    user_name = db.Column(db.String(32), unique=True, nullable=False, comment='用户名')
    user_password = db.Column(db.String(255), nullable=False, comment='密码')

    def __init__(self, user_name, user_password):
        self.user_name = user_name
        self.user_password = user_password

    def keys(self):
        return ['user_id', 'user_name']

    def __getitem__(self, item):
        return getattr(self, item)

    def __repr__(self):
        return '<User user_name: {}>'.format(self.user_name)