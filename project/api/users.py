import os

from flask import Blueprint, jsonify, request

from project.api.models import User


users_blueprint = Blueprint('users', __name__, template_folder='./templates')


@users_blueprint.route('/users/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!',
        'container_id': os.uname()[1]
    })


@users_blueprint.route('/users', methods=['GET'])
def get_all_users():
    """Get all users"""
    response_object = {
        'status': 'success',
        'users': [user.to_json() for user in User.query.all()],
        'container_id': os.uname()[1]
    }
    return jsonify(response_object), 200
