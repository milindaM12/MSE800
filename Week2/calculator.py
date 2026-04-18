import math
import cmath

# ----------------------------
# Basic Operations
# ----------------------------

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def modulus(a, b):
    return a % b

# ----------------------------
# Complex Number Operations
# ----------------------------

def add_complex(a, b):
    return complex(a) + complex(b)

def multiply_complex(a, b):
    return complex(a) * complex(b)

# ----------------------------
# Factorial Function
# ----------------------------

def factorial(n):
    if n < 0:
        return "Error: Negative number"
    return math.factorial(n)

# 
# Demo / Test Section
# 

if __name__ == "__main__":
    print("Basic Operations:")
    print("Add:", add(10, 5))
    print("Subtract:", subtract(10, 5))
    print("Multiply:", multiply(10, 5))
    print("Divide:", divide(10, 5))
    print("Modulus:", modulus(10, 5))

    print("\nComplex Operations:")
    print("Add Complex:", add_complex(2+3j, 1+4j))
    print("Multiply Complex:", multiply_complex(2+3j, 1+4j))

    print("\nFactorial:")
    print("Factorial of 5:", factorial(5))