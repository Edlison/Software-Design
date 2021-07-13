# @Author  : Edlison
# @Date    : 7/12/21 10:04
from backend.api import init_app
from backend.socket import socketio


app = init_app(socketio)


if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000)
