# @Author  : Edlison
# @Date    : 7/12/21 10:04
from backend.api import init_app
from flask_socketio import SocketIO, emit, join_room
from flask import g, session, make_response


app = init_app()
socketio = SocketIO(app)


@app.after_request
def set_header(resp):
    resp = make_response(resp)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


@socketio.on('init event')
def connet(data):
    room_id = data['room_id']
    join_room(room_id)


@socketio.on('send event')
def pair_chat(data):
    print('data ', data)
    user_name = data['user_name']
    msg = data['msg']
    room_id = data['room_id']

    ret_data = {
        'user_name': user_name,
        'message': msg
    }
    emit('receive event', ret_data, broadcast=True, to=room_id)


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
    # app.run(host='0.0.0.0', port=5000)
