# main.py

from admin import Admin
from zoo import Zoo


# Create admin user
admin = Admin("admin", "1234")

# Create zoo object
zoo = Zoo(admin)


while True:
    print("=" * 40)
    print("      ZOO APPLICATION SYSTEM")
    print("=" * 40)
    print("1. Login")
    print("2. View Animals")
    print("3. Add Animal")
    print("4. Logout")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        username = input("Enter username: ")
        password = input("Enter password: ")
        admin.login(username, password)

    elif choice == "2":
        zoo.view_animals()

    elif choice == "3":
        animal_name = input("Enter animal name: ")
        zoo.add_animal(animal_name)

    elif choice == "4":
        admin.logout()

    elif choice == "5":
        print("\nExiting application...")
        break

    else:
        print("\nInvalid choice. Please try again.\n")