# @Author  : Edlison
# @Date    : 7/12/21 12:14
import os
from datetime import timedelta


class Config:
    DIALECT = 'mysql'
    DRIVER = 'pymysql'
    USERNAME = 'chatroom'
    PASSWORD = 'chatroom'
    HOST = '121.4.249.118'
    PORT = '3306'
    DATABASE = 'chatroom'
    SECRET_KEY = os.urandom(24)
    SESSION_COOKIE_NAME = 'chatroom-session'
    PERMANENT_SESSION_LIFETIME = timedelta(days=1)
    SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}'.format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE)
    SQLALCHEMY_TRACK_MODIFICATIONS = True