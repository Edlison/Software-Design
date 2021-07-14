# @Author  : Edlison
# @Date    : 7/12/21 10:04
from backend.api import init_app
from flask_socketio import SocketIO, emit, join_room
from flask import g, session, make_response, render_template


app = init_app()
socketio = SocketIO(app, cors_allowed_origins='*')


@app.after_request
def set_header(resp):
    resp = make_response(resp)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')


@app.route('/register', methods=['GET'])
def reg():
    return render_template('register.html')


@app.route('/welcome', methods=['GET'])
def welcome():
    return render_template('welcome.html')


@socketio.on('init event')
def connet(data):
    room_id = data['room_id']
    join_room(room_id)


@socketio.on('send event')
def pair_chat(data):
    print('data ', data)
    user_name = session.get('user_name')
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
