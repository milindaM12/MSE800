# main.py

from rectangle import Rectangle

def main():
    print("=== Rectangle Calculator ===")

    try:
        length = float(input("Enter the length: "))
        width = float(input("Enter the width: "))

        rect = Rectangle(length, width)

        area = rect.calculate_area()
        perimeter = rect.calculate_perimeter()

        print(f"\nArea: {area}")
        print(f"Perimeter: {perimeter}")

    except ValueError:
        print("Invalid input! Please enter numeric values.")

if __name__ == "__main__":
    main()