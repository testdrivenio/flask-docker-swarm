import os
import logging

from flask import Blueprint, jsonify, request


LOGGER = logging.getLogger('gunicorn.error')
SECRET_CODE = open('/run/secrets/secret_code', 'r').read().strip()

main_blueprint = Blueprint('main', __name__)


@main_blueprint.route('/ping', methods=['GET'])
def ping_pong():
    LOGGER.info('Hitting the "/ping" route')
    return jsonify({
        'status': 'success',
        'message': 'pong!',
        'container_id': os.uname()[1]
    })


@main_blueprint.route('/secret', methods=['POST'])
def secret():
    LOGGER.info('Hitting the "/secret" route')
    response_object = {
        'status': 'success',
        'message': 'nay!',
        'container_id': os.uname()[1]
    }
    if request.get_json().get('secret') == SECRET_CODE:
        response_object['message'] = 'yay!'
    return jsonify(response_object)
