# Creating sets
s1 = {1, 2, 3, 4, 5}
s2 = {"apple", "banana", "cherry"}
s3 = set([10, 20, 30, 40])

print(s1)
print(s2)
print(s3)

# Adding elements
s1.add(6)
s2.add("orange")
print(s1)
print(s2)

# Removing elements
s1.remove(3)
s2.discard("banana")
print(s1)
print(s2)

# Discard vs remove
s1.discard(100)  # No error
try:
    s1.remove(100)  # Raises error
except KeyError as e:
    print("Error:", e)

# Pop random element
print(s1.pop())

# Clearing set
temp = {1, 2, 3}
temp.clear()
print(temp)

# Union
a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))
print(a | b)

# Intersection
print(a.intersection(b))
print(a & b)

# Difference
print(a.difference(b))
print(a - b)

# Symmetric difference
print(a.symmetric_difference(b))
print(a ^ b)

# Subset and superset
x = {1, 2}
y = {1, 2, 3, 4}
print(x.issubset(y))
print(y.issuperset(x))

# Disjoint
z = {7, 8, 9}
print(x.isdisjoint(z))

# Set comprehension
squares = {n**2 for n in range(6)}
print(squares)

# Frozen set
fs = frozenset([1, 2, 3, 3, 2, 1])
print(fs)

# Iterating set
for item in s2:
    print(item)

# Membership check
print("apple" in s2)
print("grape" not in s2)

# Length
print(len(s2))

# Converting list to set
lst = [1, 2, 2, 3, 4, 4, 5]
unique = set(lst)
print(unique)

# Converting string to set
s = "mississippi"
letters = set(s)
print(letters)

# Copying sets
s_copy = s1.copy()
print(s_copy)

# Updating set with multiple values
s1.update([7, 8, 9])
print(s1)

# Intersection update
c = {1, 2, 3}
d = {2, 3, 4}
c.intersection_update(d)
print(c)

# Difference update
e = {1, 2, 3}
f = {2}
e.difference_update(f)
print(e)

# Symmetric difference update
g = {1, 2, 3}
h = {3, 4}
g.symmetric_difference_update(h)
print(g)
