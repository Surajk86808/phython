# Creating tuples
t1 = (1, 2, 3, 4)
t2 = ("apple", "banana", "cherry")
t3 = (1, "hello", 3.14, True)

# Single element tuple (must have comma)
single = (5,)
print(type(single))

# Accessing elements
print(t1[0])
print(t2[-1])

# Nested tuples
nested = (1, (2,3), (4,5,6))
print(nested[1][1])

# Slicing tuples
print(t1[1:3])
print(t2[:2])
print(t1[2:])

# Tuple unpacking
a, b, c, d = t1
print(a, b, c, d)

# Using * in unpacking
nums = (10, 20, 30, 40, 50)
x, *y, z = nums
print(x, y, z)

# Concatenation
new_tup = t1 + t2
print(new_tup)

# Repetition
print(t2 * 2)

# Membership
print("apple" in t2)
print(100 not in t1)

# Iteration
for item in t2:
    print(item)

# Tuple length
print(len(t1))
print(len(t3))

# Min, Max, Sum
print(min(t1))
print(max(t1))
print(sum(t1))

# Nested tuple iteration
for row in nested:
    print(row)

# Tuple in dictionary keys
d = {("x",1): "point1", ("y",2): "point2"}
print(d[("x",1)])

# Using tuples in sets
s = {(1,2), (3,4), (1,2)}
print(s)

# Swapping values using tuples
a, b = 10, 20
a, b = b, a
print(a, b)

# Return multiple values from function using tuple
def min_max_sum(numbers):
    return min(numbers), max(numbers), sum(numbers)

result = min_max_sum([1,2,3,4,5])
print(result)

# Checking immutability
try:
    t1[0] = 99
except TypeError as e:
    print("Error:", e)

# Tuple with list inside (mutable object inside tuple)
t4 = (1, [2,3], 4)
t4[1].append(5)
print(t4)

# Tuple comprehension is not directly possible -> but generator
gen = (x*x for x in range(5))
print(tuple(gen))

# Counting elements
t5 = (1,2,2,3,3,3,4,4,4,4)
print(t5.count(2))
print(t5.count(3))
print(t5.count(5))

# Finding index
print(t5.index(3))
# print(t5.index(10)) -> ValueError

# Nested tuple unpacking
t6 = (1,(2,3))
a,(b,c) = t6
print(a,b,c)

# Comparing tuples
print((1,2,3) < (1,2,4))
print((1,3) > (1,2,9))

# Tuple sorting (by converting to list)
t7 = (5,2,9,1)
sorted_list = sorted(t7)
print(tuple(sorted_list))

# Zipping lists into tuple
names = ["Alice","Bob","Charlie"]
ages = [25,30,35]
zipped = list(zip(names,ages))
print(zipped)

# Unzipping tuples
unzipped_names, unzipped_ages = zip(*zipped)
print(unzipped_names)
print(unzipped_ages)

# Tuples with repetition in sorting
t8 = ("banana","apple","cherry","apple")
print(sorted(t8))

# Tuple as record
student = ("John", 21, "Computer Science")
print(f"Name: {student[0]}, Age: {student[1]}, Major: {student[2]}")

# Nested tuples as matrix
matrix = ((1,2,3),(4,5,6),(7,8,9))
for row in matrix:
    print(row)

# Flatten tuple of tuples
flat = tuple(x for row in matrix for x in row)
print(flat)

# Tuple with booleans
bools = (True, False, True, True)
print(all(bools))
print(any(bools))

# Sorting tuple of tuples by element
pairs = ((2,5),(1,7),(3,1))
print(sorted(pairs, key=lambda x:x[1]))

# Tuple repetition in loop
t9 = ("Hi",) * 5
for val in t9:
    print(val)

# Checking tuple immutability with id
t10 = (1,2,3)
print(id(t10))
t10 = (1,2,3,4)  # new tuple, different id
print(id(t10))

# Tuple with mixed datatypes
mix = (1,"two",3.0, [4,5])
print(mix)

# Tuple in list
lst = [(1,2),(3,4),(5,6)]
for pair in lst:
    print(pair[0], pair[1])

# Generator to tuple
t11 = tuple(i for i in range(10) if i%2==0)
print(t11)

# Using tuple() constructor
t12 = tuple("hello")
print(t12)

# Checking immutability with hash()
print(hash((1,2,3)))
# print(hash([1,2,3])) -> TypeError

# Dictionary with tuple values
grades = {"Math": (90, 85, 88), "Science": (75, 80, 95)}
for subject, marks in grades.items():
    print(subject, "avg:", sum(marks)/len(marks))

# Using enumerate with tuple
for i, val in enumerate(("a","b","c")):
    print(i, val)

# Tuple multiplication with unpacking
a, b, *rest = (1,2,3,4,5,6)
print(a, b, rest)

# Nested tuples with conditions
nested_tup = ((1,2),(3,4),(5,6))
filtered = tuple(x for pair in nested_tup for x in pair if x%2==0)
print(filtered)

# Infinite repetition using itertools
import itertools
rep = itertools.islice(itertools.cycle((1,2,3)), 10)
print(tuple(rep))

# Tuple in function args (*args)
def add_all(*args):
    return sum(args)

print(add_all(1,2,3,4,5))

# Tuple in kwargs (**kwargs)
def intro(**kwargs):
    return tuple(kwargs.items())

print(intro(name="Alice", age=22))

# Tuple comprehension with condition
evens = tuple(i for i in range(20) if i%2==0)
print(evens)

# Immutable data safety
config = ("localhost", 8080, "admin")
print(config)
