# zoo.py

from decorators import login_required


class Zoo:
    def __init__(self, admin):
        self.admin = admin
        self.animals = ["Lion", "Tiger", "Elephant"]

    @login_required
    def view_animals(self):
        print("\nAnimals in the Zoo:")
        for animal in self.animals:
            print(f"- {animal}")

    @login_required
    def add_animal(self, animal_name):
        self.animals.append(animal_name)
        print(f"\n{animal_name} added successfully!\n")

    @property
    def logged_in(self):
        return self.admin.logged_in