# @Author  : Edlison
# @Date    : 7/12/21 21:54
from backend.api.chat import chat_bp
from backend.filter.login_filter import need_login
from backend.result.system_result import SystemResult
from flask import request, session, g, render_template, jsonify
from app import socketio


@chat_bp.route('/')
def index():
    return render_template('index.html')


@chat_bp.route('/room', methods=['POST'])
def init_room():
    user_id = session.get('user_id')
    user_name = session.get('user_name')
    room_id = request.form.get('room_id')
    print('room id ', room_id)
    g.user_id = user_id
    g.user_name = user_name
    g.room_id = room_id
    res = SystemResult().ok()
    return jsonify(dict(res))
