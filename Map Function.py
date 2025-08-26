# Basic map usage with function
def square(x):
    return x*x

nums = [1, 2, 3, 4, 5]
squared = list(map(square, nums))
print(squared)

# Using lambda with map
nums2 = [6, 7, 8, 9]
squared2 = list(map(lambda x: x**2, nums2))
print(squared2)

# Map with multiple lists
a = [1, 2, 3]
b = [4, 5, 6]
sum_ab = list(map(lambda x, y: x+y, a, b))
print(sum_ab)

# Map with string functions
words = ["hello", "world", "python"]
upper_words = list(map(str.upper, words))
print(upper_words)

# Map with int conversion
str_nums = ["10", "20", "30"]
int_nums = list(map(int, str_nums))
print(int_nums)

# Map with float conversion
str_floats = ["1.5", "2.7", "3.14"]
float_nums = list(map(float, str_floats))
print(float_nums)

# Map with len function
phrases = ["Python", "Data Science", "AI"]
lengths = list(map(len, phrases))
print(lengths)

# Map with multiple transformations
nums3 = [1,2,3,4,5]
result = list(map(lambda x: x*2, nums3))
print(result)

# Map with nested functions
def add_one(x):
    return x+1
def square(x):
    return x*x
final = list(map(square, map(add_one, nums3)))
print(final)

# Map with user-defined function and lambda
def cube(x):
    return x**3
cubes = list(map(lambda x: cube(x), nums3))
print(cubes)

# Map with multiple iterables
list1 = [1,2,3]
list2 = [4,5,6]
list3 = [7,8,9]
sum_all = list(map(lambda x,y,z: x+y+z, list1, list2, list3))
print(sum_all)

# Map with string formatting
names = ["Alice", "Bob", "Charlie"]
greeted = list(map(lambda n: f"Hello {n}", names))
print(greeted)

# Map with boolean check
nums4 = [10, 15, 20, 25]
is_even = list(map(lambda x: x%2==0, nums4))
print(is_even)

# Map with complex operation
nums5 = [1,2,3,4,5]
processed = list(map(lambda x: x**2 + 3*x + 1, nums5))
print(processed)

# Map with nested list
nested = [[1,2],[3,4],[5,6]]
flat_sum = list(map(lambda x: sum(x), nested))
print(flat_sum)

# Map with conditional inside lambda
nums6 = [1,2,3,4,5]
labels = list(map(lambda x: "Even" if x%2==0 else "Odd", nums6))
print(labels)
