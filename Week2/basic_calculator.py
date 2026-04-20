class Calculator:
    # Method 1: Addition
    def add(self, a, b):
        return a + b

    # Method 2: Subtraction
    def subtract(self, a, b):
        return a - b

    # Method 3: Multiplication
    def multiply(self, a, b):
        return a * b

    # Method 4: Division (extra method for completeness)
    def divide(self, a, b):
        if b == 0:
            return "Cannot divide by zero"
        return a / b


# Function 1: Get user input
def get_numbers():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    return a, b


# Function 2: Display menu and process operations
def run_calculator():
    calc = Calculator()

    while True:
        print("\n--- Simple Calculator ---")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "5":
            print("Exiting calculator...")
            break

        a, b = get_numbers()

        if choice == "1":
            print("Result:", calc.add(a, b))
        elif choice == "2":
            print("Result:", calc.subtract(a, b))
        elif choice == "3":
            print("Result:", calc.multiply(a, b))
        elif choice == "4":
            print("Result:", calc.divide(a, b))
        else:
            print("Invalid choice!")


# Entry point
if __name__ == "__main__":
    run_calculator()