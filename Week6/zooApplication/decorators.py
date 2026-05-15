# decorators.py

def login_required(func):
    """
    Decorator that checks whether the admin is logged in.
    """

    def wrapper(self, *args, **kwargs):
        if not self.logged_in:
            print("\nAccess denied! Please login first.\n")
            return
        return func(self, *args, **kwargs)

    return wrapper