# Basic filter usage with function
def is_even(x):
    return x % 2 == 0

nums = [1,2,3,4,5,6]
evens = list(filter(is_even, nums))
print(evens)

# Using lambda with filter
nums2 = [10,15,20,25,30]
evens2 = list(filter(lambda x: x%2==0, nums2))
print(evens2)

# Filtering odd numbers
odds = list(filter(lambda x: x%2!=0, nums2))
print(odds)

# Filtering strings
words = ["apple", "banana", "kiwi", "cherry"]
long_words = list(filter(lambda w: len(w)>4, words))
print(long_words)

# Filtering vowels in a string
chars = "hello world"
vowels = list(filter(lambda c: c in "aeiou", chars))
print(vowels)

# Filtering negative numbers
nums3 = [-5, -1, 0, 3, 8, -2]
negatives = list(filter(lambda x: x<0, nums3))
print(negatives)

# Filtering positive numbers
positives = list(filter(lambda x: x>=0, nums3))
print(positives)

# Filtering with multiple conditions
nums4 = list(range(20))
filtered = list(filter(lambda x: x%2==0 and x%3==0, nums4))
print(filtered)

# Filtering with nested list
matrix = [[1,2,3],[4,5,6],[7,8,9]]
rows_with_even = list(filter(lambda row: any(x%2==0 for x in row), matrix))
print(rows_with_even)

# Filter None values
data = [0,1,None,2,None,3,False]
filtered_data = list(filter(None, data))
print(filtered_data)

# Filter dictionary keys
d = {"a":1, "b":0, "c":3}
nonzero_keys = list(filter(lambda k: d[k]!=0, d))
print(nonzero_keys)

# Filter with strings containing 'a'
fruits = ["apple","banana","cherry","kiwi"]
with_a = list(filter(lambda f: "a" in f, fruits))
print(with_a)

# Filter by length
names = ["Al","Bob","Charlie","Dan"]
long_names = list(filter(lambda x: len(x)>3, names))
print(long_names)

# Using filter with map
nums5 = list(range(10))
squared_evens = list(filter(lambda x: x%2==0, map(lambda x:x**2, nums5)))
print(squared_evens)

# Filtering tuples
pairs = [(1,2),(3,4),(5,6),(7,8)]
filtered_pairs = list(filter(lambda p: p[0]+p[1]>7, pairs))
print(filtered_pairs)

# Filtering with custom function
def divisible_by_3(x):
    return x%3==0

nums6 = list(range(1,16))
div3 = list(filter(divisible_by_3, nums6))
print(div3)

# Filter truthy values
values = [0, "", None, "Hello", 42, False]
truthy = list(filter(bool, values))
print(truthy)
