# Basic lambda function
square = lambda x: x*x
print(square(5))

# Lambda with multiple arguments
add = lambda a, b: a + b
print(add(3, 7))

# Lambda inside a list
funcs = [lambda x: x+1, lambda x: x*2, lambda x: x**2]
for f in funcs:
    print(f(5))

# Using lambda with map
nums = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, nums))
print(squared)

# Using lambda with filter
evens = list(filter(lambda x: x%2==0, nums))
print(evens)

# Using lambda with reduce
from functools import reduce
sum_all = reduce(lambda a,b: a+b, nums)
print(sum_all)

# Lambda returning string
greet = lambda name: f"Hello, {name}"
print(greet("Alice"))

# Lambda with condition
is_even = lambda x: "Even" if x%2==0 else "Odd"
print(is_even(10))
print(is_even(7))

# Lambda with default argument
power = lambda x, n=2: x**n
print(power(5))
print(power(2,3))

# Lambda in a dictionary
operations = {
    "add": lambda a,b: a+b,
    "sub": lambda a,b: a-b,
    "mul": lambda a,b: a*b
}
print(operations["add"](10,5))
print(operations["mul"](3,7))

# Lambda with sorting
words = ["apple", "banana", "cherry", "kiwi"]
words_sorted = sorted(words, key=lambda x: len(x))
print(words_sorted)

# Lambda in list comprehension
nums_squared = [(lambda x: x**2)(x) for x in range(5)]
print(nums_squared)

# Lambda inside another function
def power_func(n):
    return lambda x: x**n

cube = power_func(3)
print(cube(4))

# Lambda with multiple conditions
check = lambda x: "FizzBuzz" if x%15==0 else "Fizz" if x%3==0 else "Buzz" if x%5==0 else str(x)
result = [check(i) for i in range(1,16)]
print(result)

# Lambda for string manipulation
to_upper = lambda s: s.upper()
print(to_upper("hello"))

# Lambda returning tuple
coords = lambda x, y: (x, y)
print(coords(3,4))

# Lambda with nested lambda
outer = lambda x: (lambda y: x+y)
add_five = outer(5)
print(add_five(10))
