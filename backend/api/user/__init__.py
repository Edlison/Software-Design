# @Author  : Edlison
# @Date    : 7/12/21 10:18
from flask import Blueprint
user_bp = Blueprint('user_bp', __name__)
from .controller import user_controller
from .model import user_model, user_relation
