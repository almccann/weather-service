from flask import jsonify, make_response
from flask_httpauth import HTTPBasicAuth
import os

auth = HTTPBasicAuth()

@auth.get_password
def get_password(user):
    username = os.getenv('BASIC_AUTH_USER')
    if user == username:
        return os.getenv('BASIC_AUTH_PASSWORD')
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)
