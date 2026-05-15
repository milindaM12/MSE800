# admin.py

class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.logged_in = False

    def login(self, username, password):
        if username == self.username and password == self.password:
            self.logged_in = True
            print("\nLogin successful!\n")
        else:
            print("\nInvalid username or password!\n")

    def logout(self):
        self.logged_in = False
        print("\nLogged out successfully!\n")