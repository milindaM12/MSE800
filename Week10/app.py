"""
Main Flask application for the User Management System.

Provides:
- User Registration
- User Authentication
- Profile Management
- Password Recovery
"""

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import session

from database import create_app
from auth import register_user
from auth import login_user
from models import User

from password_reset import generate_reset_token
from password_reset import reset_password

app = create_app()


@app.route("/")
def home():
    """
    Redirect users to the login page.
    """
    return redirect("/login")


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    Handle user registration requests.

    GET:
        Display registration form.

    POST:
        Create a new user account.
    """

    if request.method == "POST":

        register_user(
            request.form["full_name"],
            request.form["dob"],
            request.form["email"],
            request.form["username"],
            request.form["password"]
        )

        return redirect("/login")

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Authenticate users and create a session.
    """

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if login_user(username, password):

            session["username"] = username

            return redirect("/profile")

    return render_template("login.html")


# @app.route("/profile")
# def profile():

#     if "username" not in session:
#         return redirect("/login")

#     return render_template(
#         "profile.html",
#         username=session["username"]
#     )

@app.route("/profile")
def profile():

    if "username" not in session:
        return redirect("/login")

    user = User.query.filter_by(
        username=session["username"]
    ).first()

    return render_template(
        "profile.html",
        user=user
    )


@app.route("/forgot-password",
           methods=["GET", "POST"])
def forgot_password():
    """
    Generate a password reset token for a user.
    """

    token = None

    if request.method == "POST":

        token = generate_reset_token(
            request.form["email"]
        )

    return render_template(
        "forgot_password.html",
        token=token
    )


@app.route("/reset-password/<token>",
           methods=["GET", "POST"])
def reset(token):
    """
    Reset a user's password using a valid token.

    Args:
        token (str): Password reset token.
    """

    if request.method == "POST":

        reset_password(
            token,
            request.form["password"]
        )

        return redirect("/login")

    return render_template(
        "reset_password.html",
        token=token
    )


if __name__ == "__main__":
    app.run(debug=True)