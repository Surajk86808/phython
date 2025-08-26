# Creating dictionaries
d1 = {"name": "Alice", "age": 25, "city": "NY"}
d2 = dict(a=1, b=2, c=3)
d3 = dict([("x", 10), ("y", 20)])

print(d1)
print(d2)
print(d3)

# Accessing values
print(d1["name"])
print(d2.get("b"))
print(d3.get("z", "Not found"))

# Modifying values
d1["age"] = 26
print(d1)

# Adding items
d1["country"] = "USA"
print(d1)

# Removing items
d1.pop("city")
print(d1)

# popitem removes last item
d2.popitem()
print(d2)

# Deleting key
del d3["x"]
print(d3)

# Iterating over dictionary
for key in d1:
    print(key, d1[key])

for key, value in d1.items():
    print(key, "->", value)

# Keys and values
print(list(d1.keys()))
print(list(d1.values()))
print(list(d1.items()))

# Checking existence
print("name" in d1)
print("city" not in d1)

# Copying dictionary
d_copy = d1.copy()
print(d_copy)

# Clearing dictionary
temp = {"a":1,"b":2}
temp.clear()
print(temp)

# Nested dictionary
students = {
    "Alice": {"age":25, "grade":"A"},
    "Bob": {"age":22, "grade":"B"}
}
print(students["Alice"]["age"])
print(students["Bob"]["grade"])

# Using setdefault
d1.setdefault("hobby", "Reading")
print(d1)

# Merging dictionaries
d4 = {"x":100}
d1.update(d4)
print(d1)

# Dictionary comprehension
squares = {x: x*x for x in range(5)}
print(squares)

# Filtering with comprehension
evens = {x: x*x for x in range(10) if x % 2 == 0}
print(evens)

# Nested dictionary comprehension
matrix = {i: {j: i*j for j in range(3)} for i in range(3)}
print(matrix)

# Dictionary with tuple keys
coord = {(0,0): "Origin", (1,2): "Point1"}
print(coord[(1,2)])

# Iterating with enumerate
for i, key in enumerate(d1):
    print(i, key, d1[key])

# Using dictionary in function
def student_info(name, **kwargs):
    return {"name": name, **kwargs}

s = student_info("Alice", age=25, grade="A")
print(s)

# Sorting dictionary by key
d_sorted = dict(sorted(squares.items()))
print(d_sorted)

# Sorting dictionary by value
d_sorted_val = dict(sorted(squares.items(), key=lambda x:x[1]))
print(d_sorted_val)

# Combining two dictionaries
d_a = {"a":1, "b":2}
d_b = {"b":3, "c":4}
combined = {**d_a, **d_b}
print(combined)
