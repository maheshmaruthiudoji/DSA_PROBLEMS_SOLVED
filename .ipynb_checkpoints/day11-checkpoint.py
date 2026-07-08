"""
Python Functions - Complete Guide

This script demonstrates:
- Defining functions
- Parameters & return values
- Default arguments
- Keyword arguments
- Variable-length arguments (*args, **kwargs)
- Lambda functions
- Recursion
"""

# 1. Basic function
def greet():
    print("Hello, Welcome!")

greet()

# 2. Function with parameters
def add(a, b):
    return a + b

print("\nAddition:", add(5, 3))

# 3. Function with default arguments
def greet_user(name="Guest"):
    print("Hello", name)

greet_user()
greet_user("Mahesh")

# 4. Keyword arguments
def student(name, marks):
    print("\nName:", name)
    print("Marks:", marks)

student(name="Mahesh", marks=95)

# 5. Return multiple values
def operations(a, b):
    return a + b, a - b

sum_val, diff_val = operations(10, 5)
print("\nSum:", sum_val, "Difference:", diff_val)

# 6. Variable-length arguments (*args)
def total(*numbers):
    return sum(numbers)

print("\nTotal using *args:", total(1, 2, 3, 4))

# 7. Keyword variable arguments (**kwargs)
def display_info(**data):
    print("\nUser Info:")
    for key, value in data.items():
        print(key, ":", value)

display_info(name="Mahesh", age=22, course="Python")

# 8. Lambda function (anonymous function)
square = lambda x: x * x
print("\nLambda square:", square(5))

# 9. Recursive function (factorial)
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print("\nFactorial of 5:", factorial(5))

# 10. Function as argument
def apply_function(func, value):
    return func(value)

print("\nFunction as argument:", apply_function(square, 6))

# 11. Local vs Global variable
x = 10

def test():
    x = 5
    print("\nLocal x:", x)

test()
print("Global x:", x)

# 12. Docstring
def info():
    """This function prints information"""
    print("\nThis is a function with docstring")

info()