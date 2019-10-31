from flask import request, jsonify, current_app
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from app import db
import jwt


def token_required(f):
    @wraps(f)
    def _verify(*args, **kwargs):
        auth_headers = request.headers.get('Authorization', '').split()

        invalid_msg = {
            'message': 'Invalid token. Registration or authentication required',
            'authenticated': False
        }
        expired_msg = {
            'message': 'Expired token. Reauthenticate required.',
            'authenticated': False
        }

        if len(auth_headers) != 2:
            return jsonify(invalid_msg), 401

        try:
            token = auth_headers[1]
            data = jwt.decode(token, current_app.config['SECRET_KEY'])
            stage = db.get_stage_by_id(data['id'])

            if not stage:
                raise RuntimeError('Этап не найден')
            return f(stage, *args, **kwargs)

        except jwt.ExpiredSignatureError:
            # 401 is Unauthorized HTTP status code
            return jsonify(expired_msg), 401

        except (jwt.InvalidTokenError, Exception) as e:
            print(e)
            return jsonify(invalid_msg), 401

    return _verify


def authenticate(data):
        id = data.get('id')
        code = data.get('code')
        if not id or not code:
            return None

        user = db.get_stage_by_id(id)
        if not user or not check_password_hash(user['hashcode'], code):
            return None

        return user
