import secrets

from models import User
from models import db
from werkzeug.security import generate_password_hash


def generate_reset_token(email):

    user = User.query.filter_by(
        email=email
    ).first()

    if not user:
        return None

    token = secrets.token_hex(16)

    user.reset_token = token

    db.session.commit()

    return token


def reset_password(token, new_password):

    user = User.query.filter_by(
        reset_token=token
    ).first()

    if not user:
        return False

    user.password = generate_password_hash(
        new_password
    )

    user.reset_token = None

    db.session.commit()

    return True