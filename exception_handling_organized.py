 
# ==================== SECTION 1: BASIC EXCEPTION HANDLING ====================

def divide(a, b):
    """Handle division with zero division error"""
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"

def access_list_element(lst, index):
    """Handle index errors when accessing list elements"""
    try:
        return lst[index]
    except IndexError:
        return "Index out of range"

def convert_to_int(value):
    """Handle value errors when converting to integer"""
    try:
        return int(value)
    except ValueError:
        return "Cannot convert to integer"

# ==================== SECTION 2: FILE OPERATION EXCEPTIONS ====================

def read_file(file_path):
    """Handle file not found errors when reading files"""
    try:
        with open(file_path, "r") as f:
            return f.read()
    except FileNotFoundError:
        return "File not found"

def write_file(file_path, data):
    """Handle IO errors when writing to files"""
    try:
        with open(file_path, "w") as f:
            f.write(data)
    except IOError:
        return "Error writing to file"

# ==================== SECTION 3: NESTED AND MULTIPLE EXCEPTIONS ====================

def nested_exceptions():
    """Example of nested exception handling"""
    try:
        x = int("hello")
    except ValueError:
        try:
            y = 10 / 0
        except ZeroDivisionError:
            return "Nested exception caught"

def multiple_exceptions(x):
    """Handle multiple exception types in one except block"""
    try:
        return 10 / x
    except (ZeroDivisionError, TypeError) as e:
        return f"Exception: {e}"

# ==================== SECTION 4: FINALLY AND ELSE CLAUSES ====================

def finally_example(x, y):
    """Demonstrate finally clause execution"""
    try:
        result = x / y
    except ZeroDivisionError:
        result = None
    finally:
        return "Finished operation"

def else_example(x, y):
    """Demonstrate else clause execution"""
    try:
        result = x + y
    except TypeError:
        return "Cannot add these types"
    else:
        return result

# ==================== SECTION 5: CUSTOM EXCEPTIONS ====================

class CustomError(Exception):
    """Custom exception class"""
    pass

def raise_custom_error(flag):
    """Raise custom exception based on condition"""
    if flag:
        raise CustomError("This is a custom error")

# ==================== SECTION 6: COMPLEX EXAMPLES ====================

def complex_example(lst, index, value):
    """Complex example with multiple exception types"""
    try:
        lst[index] = int(value)
    except (IndexError, ValueError) as e:
        return f"Error: {e}"
    else:
        return lst

# ==================== SECTION 7: DEMONSTRATION AND TESTING ====================

if __name__ == "__main__":
    print("=== BASIC EXCEPTION HANDLING TESTS ===")
    for i in range(5):
        try:
            if i % 2 == 0:
                print(f"divide(10, {i}): {divide(10, i)}")
            else:
                print(f"access_list_element([1,2,3], {i}): {access_list_element([1,2,3], i)}")
        except Exception as e:
            print(e)

    print("\n=== TYPE CONVERSION TESTS ===")
    values = ["10", "abc", "30"]
    for val in values:
        print(f"convert_to_int('{val}'): {convert_to_int(val)}")

    print("\n=== FILE OPERATION TESTS ===")
    files = ["existing.txt", "missing.txt"]
    for file in files:
        print(f"read_file('{file}'): {read_file(file)}")

    print("\n=== NESTED AND MULTIPLE EXCEPTION TESTS ===")
    print(f"nested_exceptions(): {nested_exceptions()}")
    print(f"multiple_exceptions(0): {multiple_exceptions(0)}")
    print(f"multiple_exceptions('abc'): {multiple_exceptions('abc')}")

    print("\n=== FINALLY AND ELSE CLAUSE TESTS ===")
    print(f"finally_example(10, 0): {finally_example(10, 0)}")
    print(f"finally_example(10, 2): {finally_example(10, 2)}")
    print(f"else_example(5, 10): {else_example(5, 10)}")
    print(f"else_example(5, 'abc'): {else_example(5, 'abc')}")

    print("\n=== CUSTOM EXCEPTION TESTS ===")
    try:
        raise_custom_error(True)
    except CustomError as e:
        print(f"CustomError caught: {e}")

    print("\n=== COMPLEX EXAMPLE TESTS ===")
    lst = [1,2,3]
    print(f"complex_example([1,2,3], 1, '5'): {complex_example(lst, 1, '5')}")
    print(f"complex_example([1,2,3], 5, '10'): {complex_example(lst, 5, '10')}")
    print(f"complex_example([1,2,3], 0, 'abc'): {complex_example(lst, 0, 'abc')}")

    print("\n=== USER INPUT EXCEPTION HANDLING ===")
    try:
        num = int(input("Enter a number: "))
    except ValueError:
        num = 0
    finally:
        print(f"Number is {num}")

    print("\n=== VARIOUS EXCEPTION TYPES DEMONSTRATION ===")
    exception_examples = [
        ("ZeroDivisionError", lambda: 10 / 0),
        ("IndexError", lambda: [1,2,3][10]),
        ("KeyError", lambda: {"a":1}["b"]),
        ("ValueError", lambda: int("abc")),
        ("TypeError", lambda: None + 5),
        ("FileNotFoundError", lambda: open("nonexistent.txt")),
        ("AttributeError", lambda: None.append(1))
    ]

    for name, func in exception_examples:
        try:
            func()
        except Exception as e:
            print(f"{name}: {e}")
