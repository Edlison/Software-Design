# @Author  : Edlison
# @Date    : 7/12/21 17:20
from backend.api.user import user_bp
from flask import request, session, jsonify, g, render_template
from backend.api.user.service.user_service import validate, register, add_friend, get_friends_all, update_tag, get_info, get_friend_room
from backend.api import db
from backend.api.user.model.user_model import User
from backend.api.user.model.user_relation import UserRelation
from backend.filter.login_filter import need_login


@user_bp.route('/register', methods=['POST'])
def r():
    """
    User register.

    Args:

    Returns:

    @Author  : Edlison
    @Date    : 7/12/21 19:49
    """
    user_name = request.form.get('user_name')
    user_password = request.form.get('user_password')
    res = register(user_name, user_password)
    return jsonify(dict(res))


@user_bp.route('/login', methods=['POST'])
def login():
    """
    用户登陆

    Args:

    Returns:

    @Author  : Edlison
    @Date    : 1/3/21 21:51
    """
    user_name = request.form.get('user_name')
    user_password = request.form.get('user_password')
    res = validate(user_name, user_password)
    if res.is_ok():
        session['user_id'] = g.user_id
        session['user_name'] = user_name
        res.ok('login success.')
        res.set_data({'user_id': g.user_id})
    else:
        res.error('username or password error.')
    return jsonify(dict(res))


@user_bp.route('/get_user_name', methods=['POST'])
@need_login
def gi():
    id = request.form.get('id')
    res = get_info(id)
    return jsonify(dict(res))


@user_bp.route('/get_friends_all', methods=['POST'])
@need_login
def gfa():
    user_id = session.get('user_id')
    res = get_friends_all(user_id)
    return jsonify(dict(res))


@user_bp.route('/get_friend_room', methods=['POST'])
@need_login
def gfr():
    user_id = session.get('user_id')
    friend_id = request.form.get('friend_id')
    res = get_friend_room(user_id, friend_id)
    return jsonify(dict(res))


@user_bp.route('/add_friend', methods=['POST'])
@need_login
def af():
    user_id = session.get('user_id')
    friend_id = request.form.get('friend_id')
    res = add_friend(user_id, friend_id)
    return jsonify(dict(res))


@user_bp.route('/change_tag', methods=['POST'])
def ct():
    user_id = session.get('user_id')
    friend_id = request.form.get('friend_id')
    new_tag = request.form.get('new_tag')
    res = update_tag(user_id, friend_id, new_tag)
    return jsonify(dict(res))





###########################


@user_bp.route('/create_all', methods=['POST'])
def create_all():
    print('create ...')
    db.create_all()
    return 'success'


@user_bp.route('/index')
def index():
    return render_template('index.html')