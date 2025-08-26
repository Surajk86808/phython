from functools import reduce

# Basic sum using reduce
nums = [1, 2, 3, 4, 5]
sum_all = reduce(lambda a, b: a + b, nums)
print(sum_all)

# Product of all elements
product = reduce(lambda a, b: a * b, nums)
print(product)

# Maximum element
maximum = reduce(lambda a, b: a if a>b else b, nums)
print(maximum)

# Minimum element
minimum = reduce(lambda a, b: a if a<b else b, nums)
print(minimum)

# Reduce with subtraction
sub_result = reduce(lambda a, b: a - b, nums)
print(sub_result)

# Reduce with division
div_result = reduce(lambda a, b: a / b, [100, 2, 5])
print(div_result)

# Concatenating strings
words = ["Python", "is", "fun"]
sentence = reduce(lambda a, b: a + " " + b, words)
print(sentence)

# Flattening a list of lists
nested = [[1,2],[3,4],[5,6]]
flat = reduce(lambda a, b: a + b, nested)
print(flat)

# Reduce with condition inside
nums2 = [1,2,3,4,5,6]
sum_even = reduce(lambda a,b: a+b if b%2==0 else a, nums2)
print(sum_even)

# Reduce with boolean logic
bools = [True, True, False, True]
all_true = reduce(lambda a,b: a and b, bools)
print(all_true)

# Reduce for maximum string length
words2 = ["apple", "banana", "kiwi", "cherry"]
longest = reduce(lambda a,b: a if len(a)>len(b) else b, words2)
print(longest)

# Reduce to find cumulative product
nums3 = [2,3,4]
cum_prod = reduce(lambda a,b: a*b, nums3)
print(cum_prod)

# Reduce with custom function
def combine(a, b):
    return f"{a}-{b}"

letters = ["A","B","C","D"]
combined = reduce(combine, letters)
print(combined)

# Reduce with initial value
nums4 = [1,2,3]
sum_with_init = reduce(lambda a,b: a+b, nums4, 10)
print(sum_with_init)

# Reduce to reverse a list
nums5 = [1,2,3,4,5]
reversed_list = reduce(lambda a,b: [b]+a, nums5, [])
print(reversed_list)

# Reduce for factorial
n = 5
factorial = reduce(lambda a,b: a*b, range(1,n+1))
print(factorial)

# Reduce to merge dictionaries
dicts = [{"a":1},{"b":2},{"c":3}]
merged = reduce(lambda a,b: {**a, **b}, dicts)
print(merged)

# Reduce with max by custom key
students = [{"name":"Alice","score":90},{"name":"Bob","score":85}]
top = reduce(lambda a,b: a if a["score"]>b["score"] else b, students)
print(top)
