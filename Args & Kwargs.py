# Using *args for arbitrary positional arguments
def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

print(add_numbers(1, 2, 3, 4, 5))
print(add_numbers(10, 20))

# Using **kwargs for arbitrary keyword arguments
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="NY")
print_info(company="Google", role="Developer")

# Combining regular arguments, *args and **kwargs
def combined_func(a, b, *args, **kwargs):
    print("a:", a)
    print("b:", b)
    print("args:", args)
    print("kwargs:", kwargs)

combined_func(1, 2, 3, 4, x=5, y=6)

# Passing list with *args
numbers = [1, 2, 3, 4]
print(add_numbers(*numbers))

# Passing dict with **kwargs
info = {"name":"Bob", "age":30}
print_info(**info)

# Example: finding max using *args
def max_value(*args):
    return max(args)

print(max_value(10, 20, 5, 40))

# Example: greeting multiple people
def greet_people(greeting, *names):
    for name in names:
        print(f"{greeting}, {name}!")

greet_people("Hello", "Alice", "Bob", "Charlie")

# Example: configure settings with **kwargs
def configure(**kwargs):
    settings = {
        "theme": "light",
        "font": "Arial",
        "size": 12
    }
    settings.update(kwargs)
    return settings

print(configure())
print(configure(theme="dark", size=16))

# Example: combining *args and **kwargs
def describe_person(*args, **kwargs):
    print("Positional info:", args)
    print("Keyword info:", kwargs)

describe_person("Alice", "Engineer", age=25, city="NY")

# Using *args in recursive function
def recursive_sum(*args):
    if len(args) == 0:
        return 0
    return args[0] + recursive_sum(*args[1:])

print(recursive_sum(1, 2, 3, 4, 5))

# Using **kwargs to set default values
def student_info(name, **kwargs):
    age = kwargs.get("age", 18)
    grade = kwargs.get("grade", "A")
    print(f"Name: {name}, Age: {age}, Grade: {grade}")

student_info("Alice", age=22)
student_info("Bob")

# Passing mixed args and kwargs to another function
def outer_func(*args, **kwargs):
    print("Sum:", sum(args))
    print("Keys:", list(kwargs.keys()))
    print("Values:", list(kwargs.values()))

outer_func(1,2,3, x=10, y=20)

# Using *args with map
nums = [1, 2, 3, 4]
results = list(map(lambda x: x*2, nums))
print(results)

# Using **kwargs in lambda
def power(**kwargs):
    return kwargs.get("base",1) ** kwargs.get("exp",2)

print(power(base=3, exp=4))
print(power(base=5))
