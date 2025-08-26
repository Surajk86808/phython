# For loop examples
for i in range(5):
    print("Number:", i)

for char in "Python":
    print("Char:", char)

for i in range(1, 11):
    print(i, "squared is", i*i)

for i in range(1, 6):
    for j in range(1, 6):
        print(i, "*", j, "=", i*j)

for i in [10, 20, 30, 40]:
    print("Item:", i)

for i in range(0, 21, 2):
    print("Even:", i)

for i in range(1, 21, 2):
    print("Odd:", i)

for i in range(1, 6):
    print("*" * i)

for i in range(5, 0, -1):
    print("*" * i)

for word in ["apple", "banana", "cherry"]:
    print(word.upper())

for i in range(3):
    for j in range(3):
        print("i:", i, "j:", j)

for i in range(1, 6):
    fact = 1
    for j in range(1, i+1):
        fact *= j
    print("Factorial of", i, "=", fact)

# While loop examples
n = 5
while n > 0:
    print("Countdown:", n)
    n -= 1

n = 1
while n <= 5:
    print("Square:", n*n)
    n += 1

count = 0
while count < 5:
    print("Hello", count)
    count += 1

i = 1
while i <= 10:
    if i % 2 == 0:
        print("Even:", i)
    else:
        print("Odd:", i)
    i += 1

num = 1
while num <= 5:
    cube = num**3
    print("Cube of", num, "=", cube)
    num += 1

# Loop with break
for i in range(1, 11):
    if i == 6:
        break
    print("Break Example:", i)

# Loop with continue
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print("Continue Example:", i)

# Nested while loop
i = 1
while i <= 3:
    j = 1
    while j <= 3:
        print("i:", i, "j:", j)
        j += 1
    i += 1

# Infinite loop with break
count = 0
while True:
    print("Looping...", count)
    count += 1
    if count == 5:
        break

# Fibonacci with while
a, b = 0, 1
count = 0
while count < 10:
    print("Fib:", a)
    a, b = b, a+b
    count += 1

# Prime numbers using for loop
for num in range(2, 21):
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break
    if prime:
        print("Prime:", num)

# Pattern printing
rows = 5
for i in range(1, rows+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

for i in range(1, rows+1):
    for j in range(1, rows+1):
        print("*", end=" ")
    print()

for i in range(rows):
    for j in range(rows - i - 1):
        print(" ", end="")
    for k in range(i+1):
        print("*", end="")
    print()

# Loop with else
for i in range(5):
    print("Iteration", i)
else:
    print("Loop finished")

i = 0
while i < 3:
    print("While iteration", i)
    i += 1
else:
    print("While finished")

# Reverse iteration
for i in reversed(range(1, 6)):
    print("Reversed:", i)

# List iteration
nums = [1, 2, 3, 4, 5]
for n in nums:
    print("List item:", n)

# Dict iteration
student = {"name": "Alice", "age": 22, "grade": "A"}
for key in student:
    print("Key:", key, "Value:", student[key])

for k, v in student.items():
    print(k, ":", v)

# Set iteration
s = {10, 20, 30}
for val in s:
    print("Set val:", val)

# Range loop practice
for i in range(10, 0, -2):
    print("Step:", i)

# While with continue
i = 0
while i < 10:
    i += 1
    if i % 3 == 0:
        continue
    print("While Continue:", i)
