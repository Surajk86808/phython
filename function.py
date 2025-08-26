# Basic function
def greet():
    print("Hello, World!")

greet()

# Function with parameters
def greet_name(name):
    print(f"Hello, {name}!")

greet_name("Alice")

# Function with default parameters
def greet_person(name="John"):
    print(f"Hi, {name}!")

greet_person()
greet_person("Bob")

# Function returning value
def add(a, b):
    return a + b

result = add(5, 10)
print(result)

# Function with multiple return values
def min_max(numbers):
    return min(numbers), max(numbers)

minimum, maximum = min_max([3, 7, 2, 9])
print(minimum, maximum)

# Function with arbitrary arguments (*args)
def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_all(1,2,3,4))

# Function with keyword arguments (**kwargs)
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="NY")

# Nested function
def outer():
    print("Outer function")
    def inner():
        print("Inner function")
    inner()

outer()

# Function inside function returning value
def outer_func(x):
    def inner_func(y):
        return y*y
    return inner_func(x)

print(outer_func(5))

# Lambda function
square = lambda x: x*x
print(square(6))

# Lambda with multiple arguments
add = lambda a, b: a + b
print(add(3,7))

# Using lambda with map
nums = [1,2,3,4]
squared = list(map(lambda x: x**2, nums))
print(squared)

# Using lambda with filter
evens = list(filter(lambda x: x%2==0, nums))
print(evens)

# Using lambda with reduce
from functools import reduce
sum_nums = reduce(lambda a,b: a+b, nums)
print(sum_nums)

# Function with docstring
def multiply(a, b):
    """Returns product of a and b"""
    return a*b

print(multiply(3,4))
print(multiply.__doc__)

# Function with type hints
def divide(a: float, b: float) -> float:
    return a / b

print(divide(10,2))

# Recursion
def factorial(n):
    if n==1:
        return 1
    return n * factorial(n-1)

print(factorial(5))

# Recursive Fibonacci
def fib(n):
    if n<=1:
        return n
    return fib(n-1) + fib(n-2)

for i in range(7):
    print(fib(i))

# Function returning function
def power_func(n):
    return lambda x: x**n

cube = power_func(3)
print(cube(4))

# Function with list comprehension
def squares_list(n):
    return [i*i for i in range(1, n+1)]

print(squares_list(5))
