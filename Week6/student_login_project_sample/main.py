from users import (
    student_login,
    submit_assignment,
    view_grades
)

# Main application function
def main():

    # Simulate student login
    student_login("Mohammad")

    submit_assignment(
        "Mohammad",
        "Python Decorator Project"
    )

    view_grades("Alex")

# Run application
if __name__ == "__main__":
    main()
