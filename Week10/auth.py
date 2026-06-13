from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

from models import User
from models import db


def register_user(
        full_name,
        dob,
        email,
        username,
        password):

    hashed_password = generate_password_hash(password)

    user = User(
        full_name=full_name,
        date_of_birth=dob,
        email=email,
        username=username,
        password=hashed_password
    )

    db.session.add(user)
    db.session.commit()


def login_user(username, password):

    user = User.query.filter_by(
        username=username
    ).first()

    if user and check_password_hash(
            user.password,
            password):
        return True

    return False