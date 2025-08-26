# Creating strings
s1 = "Hello"
s2 = 'World'
s3 = """This is
a multi-line
string"""
print(s1, s2, s3)

# Accessing characters
print(s1[0])
print(s2[-1])

# Slicing strings
print(s1[1:4])
print(s2[:3])
print(s3[5:15])

# String length
print(len(s1), len(s3))

# String concatenation
s4 = s1 + " " + s2
print(s4)

# Repetition
print(s1 * 3)

# Iterating over string
for ch in s1:
    print(ch)

# Checking membership
print("H" in s1)
print("z" not in s2)

# String methods
print(s1.upper())
print(s2.lower())
print(s1.capitalize())
print(s2.title())

# Stripping
s5 = "  python  "
print(s5.strip())
print(s5.lstrip())
print(s5.rstrip())

# Replace
s6 = "I like apples"
print(s6.replace("apples", "oranges"))

# Splitting
words = s6.split()
print(words)

# Joining
joined = "-".join(words)
print(joined)

# Startswith / endswith
print(s6.startswith("I"))
print(s6.endswith("oranges"))

# Find / index
print(s6.find("like"))
print(s6.find("banana"))
try:
    print(s6.index("banana"))
except ValueError as e:
    print("Error:", e)

# Count
print(s6.count("a"))

# isdigit / isalpha / isalnum
print("123".isdigit())
print("abc".isalpha())
print("abc123".isalnum())

# Formatting strings
name = "Alice"
age = 25
print("My name is {} and I am {}".format(name, age))
print(f"My name is {name} and I am {age}")

# Escaping characters
s7 = "I\'m learning Python"
print(s7)
s8 = "Line1\nLine2"
print(s8)

# Reversing string
print(s1[::-1])

# String comparison
print("apple" < "banana")
print("abc" == "abc")

# Nested formatting
num = 3.14159
print(f"Pi value: {num:.2f}")

# Multi-line string formatting
info = f"""
Name: {name}
Age: {age}
"""
print(info)

# Splitting and iterating
for word in s6.split():
    print(word)

# Joining characters
chars = ['a','b','c']
print("".join(chars))
