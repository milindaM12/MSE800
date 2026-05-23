from abc import ABC, abstractmethod


# =========================
# Abstract Fish Class
# =========================
class Fish(ABC):

    @abstractmethod
    def category(self):
        pass


# =========================
# Fish Types
# =========================
class Goldfish(Fish):

    def category(self):
        return "Freshwater"


class Shark(Fish):

    def category(self):
        return "Saltwater Predator"


class Angelfish(Fish):

    def category(self):
        return "Freshwater Tropical"


class Tuna(Fish):

    def category(self):
        return "Saltwater"


class Salmon(Fish):

    def category(self):
        return "Migratory Fish"


# =========================
# Factory Design Pattern
# =========================
class FishFactory:

    @staticmethod
    def create_fish(fish_type):

        fish_type = fish_type.lower()

        if fish_type == "goldfish":
            return Goldfish()

        elif fish_type == "shark":
            return Shark()

        elif fish_type == "angelfish":
            return Angelfish()

        elif fish_type == "tuna":
            return Tuna()

        elif fish_type == "salmon":
            return Salmon()

        else:
            raise ValueError("Invalid fish type")


# =========================
# Singleton Design Pattern
# =========================
class AquariumManager:

    __instance = None

    def __new__(cls):

        if cls.__instance is None:
            cls.__instance = super(AquariumManager, cls).__new__(cls)

            cls.__instance.inventory = {
                "Goldfish": 0,
                "Shark": 0,
                "Angelfish": 0,
                "Tuna": 0,
                "Salmon": 0
            }

        return cls.__instance

    def add_fish(self, fish_name):

        fish = FishFactory.create_fish(fish_name)

        proper_name = fish_name.capitalize()

        self.inventory[proper_name] += 1

        print(f"{proper_name} added successfully")
        print(f"Category: {fish.category()}")

    def display_inventory(self):

        print("\n===== Aquarium Inventory =====")

        for fish, count in self.inventory.items():
            print(f"{fish}: {count}")

        print("==============================\n")


# =========================
# Main Program
# =========================
def main():

    aquarium = AquariumManager()

    while True:

        print("Aquarium Management System")
        print("1. Add Fish")
        print("2. Display Inventory")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":

            fish_name = input(
                "Enter fish type "
                "(Goldfish, Shark, Angelfish, Tuna, Salmon): "
            )

            try:
                aquarium.add_fish(fish_name)

            except ValueError as e:
                print(e)

        elif choice == "2":
            aquarium.display_inventory()

        elif choice == "3":
            print("Exiting Aquarium System...")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()