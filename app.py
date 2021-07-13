# @Author  : Edlison
# @Date    : 7/12/21 10:04
from backend.api import init_app
from flask_socketio import SocketIO, emit, join_room
from flask import g, session


app = init_app()
socketio = SocketIO(app)


@socketio.on('send event')
def pair_chat(data):
    print('data ', data)
    msg = data['msg']
    room_id = data['room_id']
    user_name = session.get('user_name')
    join_room(room_id)
    print('msg ', msg)
    print('room_id ', room_id)
    if not user_name:
        user_name = 'default'
    print('user name ', user_name)
    ret_data = {
        'user_name': user_name,
        'message': msg
    }
    emit('receive event', ret_data, broadcast=True, to=room_id)


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
    # app.run(host='0.0.0.0', port=5000)
