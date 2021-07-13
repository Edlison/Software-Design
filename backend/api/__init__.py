# @Author  : Edlison
# @Date    : 7/12/21 10:18
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config


db = SQLAlchemy()


def init_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    from .user import user_bp
    app.register_blueprint(user_bp, url_prefix='/api/user')
    from .chat import chat_bp
    app.register_blueprint(chat_bp, url_prefix='/api/chat')

    return app