# Creating lists
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]
mixed = [1, "hello", 3.14, True]

# Accessing elements
print(numbers[0])
print(fruits[-1])

# Modifying elements
numbers[2] = 30
print(numbers)

# Adding elements
numbers.append(6)
numbers.insert(2, 100)
print(numbers)

# Removing elements
numbers.remove(100)
last = numbers.pop()
print(last, numbers)

# Iterating over a list
for fruit in fruits:
    print(fruit)

# Checking membership
print("apple" in fruits)
print("grape" not in fruits)

# List length
print(len(numbers))
print(len(fruits))

# Concatenation
all_items = numbers + fruits
print(all_items)

# Repetition
print(fruits * 2)

# Slicing
print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])

# Copying lists
copy_numbers = numbers[:]
print(copy_numbers)

# Sorting
nums = [10, 2, 33, 4, 5]
nums.sort()
print(nums)

nums.sort(reverse=True)
print(nums)

# Using sorted()
print(sorted(fruits))
print(sorted(fruits, reverse=True))

# Min, Max, Sum
print(min(nums))
print(max(nums))
print(sum(nums))

# List Comprehension - squares
squares = [x**2 for x in range(10)]
print(squares)

# Even numbers using list comprehension
evens = [x for x in range(20) if x % 2 == 0]
print(evens)

# Odd numbers using list comprehension
odds = [x for x in range(20) if x % 2 != 0]
print(odds)

# Strings to uppercase
upper_fruits = [fruit.upper() for fruit in fruits]
print(upper_fruits)

# Filter numbers > 10
big_nums = [x for x in nums if x > 10]
print(big_nums)

# Nested list comprehension
pairs = [(x, y) for x in [1,2,3] for y in [4,5,6]]
print(pairs)

# Flatten a nested list
matrix = [[1,2,3],[4,5,6],[7,8,9]]
flat = [num for row in matrix for num in row]
print(flat)

# Conditional expression
labels = ["even" if i%2==0 else "odd" for i in range(10)]
print(labels)

# Cartesian product
A = [1, 2, 3]
B = ['a', 'b']
cartesian = [(x,y) for x in A for y in B]
print(cartesian)

# Remove duplicates using list comprehension
nums = [1,2,2,3,4,4,5]
unique = []
[unique.append(x) for x in nums if x not in unique]
print(unique)

# Reverse list
print(numbers[::-1])

# Nested comprehension for multiplication table
table = [[i*j for j in range(1,6)] for i in range(1,6)]
print(table)

# Prime numbers comprehension
primes = [x for x in range(2,50) if all(x % y != 0 for y in range(2, int(x**0.5)+1))]
print(primes)

# Fibonacci using list comprehension (limited terms)
fib = [0,1]
[fib.append(fib[-1]+fib[-2]) for _ in range(8)]
print(fib)

# Remove vowels from string using list comprehension
word = "comprehension"
no_vowels = "".join([ch for ch in word if ch not in "aeiou"])
print(no_vowels)

# Multiple conditions
filtered = [x for x in range(30) if x % 2 == 0 if x % 3 == 0]
print(filtered)

# Nested loops in comprehension
matrix_2 = [[i+j for j in range(3)] for i in range(3)]
print(matrix_2)

# Dictionary from list comprehension
squares_dict = {x: x**2 for x in range(6)}
print(squares_dict)

# Set from list comprehension
set_squares = {x**2 for x in range(6)}
print(set_squares)

# List comprehension with functions
def cube(n): return n**3
cubes = [cube(i) for i in range(10)]
print(cubes)

# Filter names starting with "a"
names = ["alice","bob","anna","mike"]
a_names = [n for n in names if n.startswith("a")]
print(a_names)

# Combine strings and numbers
combos = [f"{n}{s}" for n in range(3) for s in "ab"]
print(combos)

# Nested conditionals
results = ["FizzBuzz" if i%15==0 else "Fizz" if i%3==0 else "Buzz" if i%5==0 else str(i) for i in range(1,21)]
print(results)

# Using enumerate in list comprehension
indexed = [(i,val) for i,val in enumerate(fruits)]
print(indexed)

# Transpose of matrix
matrix = [[1,2,3],[4,5,6]]
transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transpose)
