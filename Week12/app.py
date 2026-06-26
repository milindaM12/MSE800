from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/welcome")
def welcome():
    return "Welcome to the Flask application!"

@app.route("/bye")
def bye():
    return "Bye Flask application!"    

# Dynamic route with string variable
@app.route("/user/<username>")
def user_profile(username):
    return f"Welcome, {username}!"

# Dynamic route with integer variable
@app.route("/post/<int:post_id>")
def show_post(post_id):
    return f"Viewing post #{post_id}"

# Multiple variables
@app.route("/user/<username>/post/<int:post_id>")
def user_post(username, post_id):
    return f"User {username} is viewing post {post_id}"



if __name__ == "__main__":
    app.run(debug=True)