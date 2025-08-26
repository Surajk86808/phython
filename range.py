# Basic range
print(list(range(5)))
print(list(range(10)))
print(list(range(0, 5)))
print(list(range(1, 6)))

# Range with step
print(list(range(0, 10, 2)))
print(list(range(1, 10, 2)))
print(list(range(10, 0, -1)))
print(list(range(20, 0, -2)))

# Using range in loops
for i in range(5):
    print("Loop:", i)

for i in range(1, 6):
    print("Number:", i)

for i in range(2, 11, 2):
    print("Even:", i)

for i in range(1, 10, 2):
    print("Odd:", i)

# Range with negative numbers
print(list(range(-5, 6)))
print(list(range(-10, 0, 2)))
print(list(range(5, -6, -1)))
print(list(range(-1, -10, -2)))

# Nested range
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)

# Range in list comprehension
squares = [x*x for x in range(1, 11)]
print(squares)

cubes = [x**3 for x in range(1, 6)]
print(cubes)

evens = [x for x in range(20) if x % 2 == 0]
print(evens)

# Range with sum
total = sum(range(1, 11))
print("Sum 1-10:", total)

# Range with max and min
print("Max:", max(range(1, 11)))
print("Min:", min(range(1, 11)))

# Range with len
print("Length:", len(range(1, 50, 5)))

# Range reversed
print(list(reversed(range(1, 6))))

for i in reversed(range(1, 6)):
    print("Reverse:", i)

# Range with enumerate
for idx, val in enumerate(range(5, 10)):
    print(idx, val)

# Range with step patterns
print(list(range(0, 50, 5)))
print(list(range(100, 50, -10)))
print(list(range(1, 100, 9)))

# Multiplication table with range
for i in range(1, 11):
    print("5 x", i, "=", 5*i)

# Factorials with range
fact = 1
for i in range(1, 6):
    fact *= i
print("Factorial 5:", fact)

# Nested range for matrix
for i in range(1, 4):
    row = []
    for j in range(1, 4):
        row.append(i*j)
    print(row)

# Triangular pattern with range
for i in range(1, 6):
    print("".join(str(x) for x in range(1, i+1)))

# Range with condition
for i in range(1, 21):
    if i % 3 == 0:
        print("Div by 3:", i)

# Prime numbers with range
for num in range(2, 21):
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break
    if prime:
        print("Prime:", num)

# Fibonacci using range
a, b = 0, 1
for _ in range(10):
    print(a)
    a, b = b, a+b

# Range with string
s = "HELLO"
for i in range(len(s)):
    print("Index", i, ":", s[i])

# Range with step filtering
print([i for i in range(1, 51) if i % 7 == 0])
print([i for i in range(1, 51) if i % 5 == 0])

# Multiplication pattern
for i in range(1, 6):
    for j in range(1, 6):
        print(i*j, end=" ")
    print()

# Range to generate coordinates
coords = [(x, y) for x in range(3) for y in range(3)]
print(coords)

# Odd square numbers
odd_squares = [x*x for x in range(1, 20, 2)]
print(odd_squares)

# Even cube numbers
even_cubes = [x**3 for x in range(2, 21, 2)]
print(even_cubes)

# Range for reverse iteration
for i in range(10, 0, -1):
    print("Reverse loop:", i)

# Nested loop diamond pattern
n = 5
for i in range(1, n+1):
    print(" "*(n-i) + "*"*i)
for i in range(n-1, 0, -1):
    print(" "*(n-i) + "*"*i)

# Generate alphabet positions
alphabets = {chr(65+i): i+1 for i in range(26)}
print(alphabets)

# Generate squares dictionary
squares_dict = {i: i*i for i in range(1, 11)}
print(squares_dict)

# Range for building multiplication table
table = {i: [i*j for j in range(1, 11)] for i in range(1, 6)}
print(table)

# Range with filtering numbers divisible by both 3 and 5
nums = [i for i in range(1, 51) if i % 3 == 0 and i % 5 == 0]
print(nums)

# Sum of squares using range
sum_squares = sum([i*i for i in range(1, 11)])
print("Sum of squares:", sum_squares)

# Range with zip
for a, b in zip(range(1, 6), range(10, 5, -1)):
    print(a, b)

# Range for Pascal triangle like
for i in range(1, 6):
    print(" "*(5-i) + " ".join(str(j) for j in range(1, i+1)))
