"""
main.py — Auckland Aquarium Management CLI
==========================================
Interactive command-line interface for managing the Auckland Aquarium.
Demonstrates both design patterns in action:
  • Singleton  → Aquarium (only one instance ever exists)
  • Factory    → FishFactory (creates fish objects by species name)
"""

from src.aquarium import Aquarium
from src.fish import FishFactory


MENU = """
╔══════════════════════════════════╗
║   Auckland Aquarium Manager      ║
╠══════════════════════════════════╣
║  1. Add fish                     ║
║  2. Remove fish                  ║
║  3. View inventory               ║
║  4. View category summary        ║
║  5. Exit                         ║
╚══════════════════════════════════╝
"""

SUPPORTED = FishFactory.supported_species()


def prompt_species() -> str:
    print(f"\n  Supported species: {', '.join(s.capitalize() for s in SUPPORTED)}")
    while True:
        species = input("  Enter species name: ").strip()
        if species.lower() in SUPPORTED:
            return species
        print(f"  ❌ '{species}' is not a supported species. Try again.")


def prompt_count(action: str = "add") -> int:
    while True:
        raw = input(f"  How many to {action}? ").strip()
        if raw.isdigit() and int(raw) >= 1:
            return int(raw)
        print("  ❌ Please enter a positive whole number.")


def main():
    # Singleton — always returns the same instance
    aquarium = Aquarium(name="Auckland Aquarium")

    # Seed some initial data to make the demo immediately interesting
    initial = [("Goldfish", 12), ("Shark", 2), ("Angelfish", 8),
               ("Tuna", 5), ("Salmon", 7)]
    for species, count in initial:
        aquarium.add_fish(species, count)

    print("\n🐠  Welcome to the Auckland Aquarium Management System  🐠")
    print(f"   Aquarium object id: {id(aquarium)}  (Singleton)\n")

    while True:
        print(MENU)
        choice = input("Select an option [1-5]: ").strip()

        if choice == "1":
            species = prompt_species()
            count = prompt_count("add")
            try:
                aquarium.add_fish(species, count)
                print(f"\n  ✅ Added {count} × {species.capitalize()} to the aquarium.")
            except ValueError as e:
                print(f"\n  ❌ {e}")

        elif choice == "2":
            species = prompt_species()
            count = prompt_count("remove")
            try:
                aquarium.remove_fish(species, count)
                print(f"\n  ✅ Removed {count} × {species.capitalize()} from the aquarium.")
            except ValueError as e:
                print(f"\n  ❌ {e}")

        elif choice == "3":
            print()
            print(aquarium.display())

        elif choice == "4":
            print("\n  Category Summary")
            print(f"  {'─'*40}")
            for category, count in sorted(aquarium.category_summary().items()):
                print(f"  {category:<35} {count:>3} fish")
            print(f"  {'─'*40}")
            print(f"  Total: {aquarium.total_fish()} fish")

        elif choice == "5":
            print("\n  Goodbye! 🐟\n")
            break

        else:
            print("  ❌ Invalid choice. Please select 1–5.")

        # Prove Singleton: every call to Aquarium() returns the same object
        same_instance = Aquarium()
        assert id(same_instance) == id(aquarium), "Singleton broken!"


if __name__ == "__main__":
    main()