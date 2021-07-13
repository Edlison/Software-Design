# @Author  : Edlison
# @Date    : 7/12/21 10:04
from flask import Blueprint
chat_bp = Blueprint('chat_bp', __name__)
from .controller import chat_controller
from .models.chatroom import Chatroom