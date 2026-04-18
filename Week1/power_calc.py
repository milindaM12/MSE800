def calculate_power(x, y):
    return x ** y

# Taking user input
x = float(input("Enter the base (x): "))
y = float(input("Enter the exponent (y): "))

result = calculate_power(x, y)

print(f"\nFinal Output: {x} raised to the power {y} is {result}")