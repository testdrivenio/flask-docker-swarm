import os
import logging

from flask import Blueprint, jsonify

from project.api.models import User


users_blueprint = Blueprint('users', __name__)

LOGGER = logging.getLogger('gunicorn.error')


@users_blueprint.route('/users', methods=['GET'])
def get_all_users():
    LOGGER.info('Hitting the "/users" route')
    response_object = {
        'status': 'success',
        'users': [user.to_json() for user in User.query.all()],
        'container_id': os.uname()[1]
    }
    return jsonify(response_object), 200
