from decorators import log_activity

# Handles student login activity
@log_activity
def student_login(username):
    print(f"{username} logged into the system.")

# Handles assignment submission activity
@log_activity
def submit_assignment(username, assignment):
    print(f"{username} submitted {assignment}.")

# Handles viewing grades activity
@log_activity
def view_grades(username):
    print(f"{username} is viewing grades.")
