# @Author  : Edlison
# @Date    : 7/12/21 18:28
from app import socketio
from flask import g
from datetime import datetime


# @socketio.on('send event')
# def pair_chat(data):
#     print('data ', data)
#     msg = data['msg']
#
#     ret_data = {
#         'user_name': g.user_name,
#         'message': msg,
#         'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#     }
#     socketio.emit('receive event', ret_data, broadcast=True)

