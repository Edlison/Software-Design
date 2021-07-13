# @Author  : Edlison
# @Date    : 7/12/21 18:28
from flask_socketio import emit
from backend.socket import socketio
from flask import g
from datetime import datetime


@socketio.on('send event', namespace='/chatroom')
def pair_chat(data):
    msg = data['msg']
    ret_data = {
        'user_name': g.user_name,
        'message': msg,
        'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    emit('receive event', ret_data, broadcast=True, to=g.room_id)

