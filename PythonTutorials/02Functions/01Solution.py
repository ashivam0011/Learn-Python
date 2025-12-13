"""
PYTHON FUNCTIONS TUTORIAL
=========================
This file contains comprehensive examples of Python functions with detailed comments.
Learn step by step from basic to advanced concepts.
"""

# ============================================================================
# 1. BASIC FUNCTION DEFINITION
# ============================================================================

def greet():
    """
    A simple function that prints a greeting.
    Functions are defined using the 'def' keyword followed by function name and parentheses.
    """
    print("Hello, World!")

# Calling the function
greet()  # Output: Hello, World!


# ============================================================================
# 2. FUNCTIONS WITH PARAMETERS
# ============================================================================

def greet_person(name):
    """
    Function with one parameter.
    Parameters are variables that receive values when the function is called.
    """
    print(f"Hello, {name}!")

greet_person("Alice")  # Output: Hello, Alice!
greet_person("Bob")    # Output: Hello, Bob!


def add_numbers(a, b):
    """
    Function with multiple parameters.
    This function takes two numbers and prints their sum.
    """
    result = a + b
    print(f"{a} + {b} = {result}")

add_numbers(5, 3)  # Output: 5 + 3 = 8
add_numbers(10, 20)  # Output: 10 + 20 = 30


# ============================================================================
# 3. FUNCTIONS WITH RETURN VALUES
# ============================================================================

def multiply(x, y):
    """
    Function that returns a value.
    Use 'return' keyword to send a value back to the caller.
    """
    
    return x * y

result = multiply(4, 5)
print(f"Result: {result}")  # Output: Result: 20

# You can use the return value directly
print(f"10 * 3 = {multiply(10, 3)}")  # Output: 10 * 3 = 30


def get_full_name(first_name, last_name):
    """
    Function can return any data type: strings, numbers, lists, dictionaries, etc.
    """
    return f"{first_name} {last_name}"

name = get_full_name("John", "Doe")
print(name)  # Output: John Doe


# ============================================================================
# 4. FUNCTIONS WITH DEFAULT PARAMETERS
# ============================================================================

def greet_with_default(name="Guest"):
    """
    Function with default parameter value.
    If no argument is provided, the default value is used.
    """
    print(f"Hello, {name}!")

greet_with_default()  # Output: Hello, Guest! (uses default)
greet_with_default("Alice")  # Output: Hello, Alice! (overrides default)


def create_profile(name, age=18, city="Unknown"):
    """
    Multiple parameters with defaults.
    Note: Parameters with defaults must come after parameters without defaults.
    """
    print(f"Name: {name}, Age: {age}, City: {city}")

create_profile("Bob")  # Output: Name: Bob, Age: 18, City: Unknown
create_profile("Alice", 25)  # Output: Name: Alice, Age: 25, City: Unknown
create_profile("Charlie", 30, "New York")  # Output: Name: Charlie, Age: 30, City: New York


# ============================================================================
# 5. KEYWORD ARGUMENTS
# ============================================================================

def calculate_total(price, tax_rate=0.1, discount=0):
    """
    Using keyword arguments allows you to specify arguments by name.
    This makes function calls more readable and allows you to skip optional parameters.
    """
    subtotal = price - (price * discount)
    total = subtotal + (subtotal * tax_rate)
    return total

# Positional arguments (order matters)
result1 = calculate_total(100, 0.15, 0.1)
print(f"Total: ${result1}")

# Keyword arguments (order doesn't matter)
result2 = calculate_total(price=100, discount=0.1, tax_rate=0.15)
print(f"Total: ${result2}")

# Mix of positional and keyword arguments
result3 = calculate_total(100, tax_rate=0.2)  # price=100 (positional), tax_rate=0.2 (keyword)
print(f"Total: ${result3}")


# ============================================================================
# 6. VARIABLE-LENGTH ARGUMENTS (*args)
# ============================================================================

def sum_all(*args):
    """
    *args allows a function to accept any number of positional arguments.
    The arguments are collected into a tuple.
    """
    total = 0
    for num in args:
        total += num
    return total

print(sum_all(1, 2, 3))  # Output: 6
print(sum_all(1, 2, 3, 4, 5))  # Output: 15
print(sum_all(10, 20, 30, 40, 50, 60))  # Output: 210


def print_info(name, *hobbies):
    """
    You can combine regular parameters with *args.
    Regular parameters must come before *args.
    """
    print(f"{name} enjoys:")
    for hobby in hobbies:
        print(f"  - {hobby}")

print_info("Alice", "reading", "swimming", "coding")
# Output:
# Alice enjoys:
#   - reading
#   - swimming
#   - coding


# ============================================================================
# 7. KEYWORD ARGUMENTS (**kwargs)
# ============================================================================

def create_student(**kwargs):
    """
    **kwargs allows a function to accept any number of keyword arguments.
    The arguments are collected into a dictionary.
    """
    print("Student Information:")
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

create_student(name="Bob", age=20, grade="A", city="Boston")
# Output:
# Student Information:
#   name: Bob
#   age: 20
#   grade: A
#   city: Boston


def process_order(item, quantity, **details):
    """
    You can combine regular parameters, *args, and **kwargs.
    Order must be: regular params, *args, **kwargs
    """
    print(f"Order: {quantity} x {item}")
    if details:
        print("Additional details:")
        for key, value in details.items():
            print(f"  {key}: {value}")

process_order("Laptop", 2, warranty="2 years", color="Silver", brand="Dell")
# Output:
# Order: 2 x Laptop
# Additional details:
#   warranty: 2 years
#   color: Silver
#   brand: Dell


# ============================================================================
# 8. LAMBDA FUNCTIONS (ANONYMOUS FUNCTIONS)
# ============================================================================

# Lambda functions are small, anonymous functions defined with the 'lambda' keyword
# Syntax: lambda arguments: expression

# Simple lambda function
square = lambda x: x ** 2
print(square(5))  # Output: 25

# Lambda with multiple arguments
add = lambda a, b: a + b
print(add(3, 4))  # Output: 7

# Lambda functions are commonly used with built-in functions like map(), filter(), sorted()
numbers = [1, 2, 3, 4, 5]

# Using lambda with map() to square all numbers
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]

# Using lambda with filter() to get even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # Output: [2, 4]

# Using lambda with sorted() to sort by a specific key
students = [("Alice", 20), ("Bob", 18), ("Charlie", 22)]
sorted_by_age = sorted(students, key=lambda x: x[1])
print(sorted_by_age)  # Output: [('Bob', 18), ('Alice', 20), ('Charlie', 22)]


# ============================================================================
# 9. RECURSIVE FUNCTIONS
# ============================================================================

def factorial(n):
    """
    A recursive function calls itself.
    Recursive functions must have a base case to avoid infinite recursion.
    """
    # Base case: factorial of 0 or 1 is 1
    if n <= 1:
        return 1
    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Output: 120 (5! = 5 * 4 * 3 * 2 * 1)


def fibonacci(n):
    """
    Another example of recursion: Fibonacci sequence.
    Each number is the sum of the two preceding ones.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(f"Fibonacci(7) = {fibonacci(7)}")  # Output: Fibonacci(7) = 13


# ============================================================================
# 10. FUNCTION SCOPE AND VARIABLES
# ============================================================================

global_var = "I'm global"  # Global variable

def demonstrate_scope():
    """
    Understanding variable scope in functions.
    """
    local_var = "I'm local"  # Local variable (only accessible inside function)
    print(f"Inside function - Global: {global_var}")
    print(f"Inside function - Local: {local_var}")

demonstrate_scope()
# print(local_var)  # This would cause an error - local_var is not accessible outside


def modify_global():
    """
    To modify a global variable inside a function, use the 'global' keyword.
    """
    global global_var
    global_var = "I've been modified!"
    print(f"Modified global: {global_var}")

modify_global()
print(f"Outside function: {global_var}")  # Output: Outside function: I've been modified!


# ============================================================================
# 11. DOCSTRINGS
# ============================================================================

def calculate_area(length, width):
    """
    Calculate the area of a rectangle.
    
    This is a docstring - it documents what the function does.
    Docstrings are written in triple quotes and should describe:
    - What the function does
    - Parameters (if any)
    - Return value (if any)
    
    Args:
        length (float): The length of the rectangle
        width (float): The width of the rectangle
    
    Returns:
        float: The area of the rectangle (length * width)
    
    Example:
        >>> calculate_area(5, 3)
        15
    """
    return length * width

# You can access the docstring using __doc__ attribute
print(calculate_area.__doc__)


# ============================================================================
# 12. TYPE HINTS (Optional but Recommended)
# ============================================================================

def add_with_hints(a: int, b: int) -> int:
    """
    Type hints help document expected parameter and return types.
    They don't enforce types but help with code clarity and IDE support.
    """
    return a + b

def process_data(name: str, age: int, is_active: bool = True) -> dict:
    """
    Function with type hints for all parameters and return value.
    """
    return {
        "name": name,
        "age": age,
        "is_active": is_active
    }

result = process_data("Alice", 25, False)
print(result)  # Output: {'name': 'Alice', 'age': 25, 'is_active': False}


# ============================================================================
# 13. FUNCTIONS AS FIRST-CLASS OBJECTS
# ============================================================================

def greet_english(name):
    return f"Hello, {name}!"

def greet_spanish(name):
    return f"¡Hola, {name}!"

def greet_french(name):
    return f"Bonjour, {name}!"

def get_greeter(language):
    """
    Functions can be returned from other functions.
    Functions are first-class objects in Python - they can be:
    - Assigned to variables
    - Passed as arguments
    - Returned from functions
    """
    greeters = {
        "english": greet_english,
        "spanish": greet_spanish,
        "french": greet_french
    }
    return greeters.get(language, greet_english)

greeter = get_greeter("spanish")
print(greeter("Alice"))  # Output: ¡Hola, Alice!

# Functions can be stored in lists, dictionaries, etc.
functions_list = [greet_english, greet_spanish, greet_french]
for func in functions_list:
    print(func("Bob"))


# ============================================================================
# 14. NESTED FUNCTIONS (INNER FUNCTIONS)
# ============================================================================

def outer_function(x):
    """
    Functions can be defined inside other functions.
    Inner functions have access to variables in the outer function's scope.
    """
    def inner_function(y):
        # Inner function can access 'x' from outer function
        return x + y
    
    return inner_function(10)

result = outer_function(5)
print(result)  # Output: 15


def multiplier(factor):
    """
    This is a closure - an inner function that remembers variables from outer scope.
    """
    def multiply(number):
        return number * factor
    return multiply

double = multiplier(2)
triple = multiplier(3)

print(double(5))  # Output: 10
print(triple(5))  # Output: 15


# ============================================================================
# 15. PRACTICAL EXAMPLES
# ============================================================================

def validate_email(email: str) -> bool:
    """
    Check if an email address is valid (simple validation).
    """
    if "@" in email and "." in email.split("@")[1]:
        return True
    return False

print(validate_email("user@example.com"))  # Output: True
print(validate_email("invalid-email"))  # Output: False


def find_max_min(numbers: list) -> tuple:
    """
    Find maximum and minimum values in a list.
    Returns a tuple of (max, min).
    """
    if not numbers:
        return None, None
    return max(numbers), min(numbers)

numbers = [3, 1, 4, 1, 5, 9, 2, 6]
max_val, min_val = find_max_min(numbers)
print(f"Max: {max_val}, Min: {min_val}")  # Output: Max: 9, Min: 1


def count_words(text: str) -> dict:
    """
    Count occurrences of each word in a text.
    """
    words = text.lower().split()
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

text = "hello world hello python world"
counts = count_words(text)
print(counts)  # Output: {'hello': 2, 'world': 2, 'python': 1}


# ============================================================================
# 16. GENERATOR FUNCTIONS
# ============================================================================

def countdown(n):
    """
    Generator functions use 'yield' instead of 'return'.
    They return an iterator that generates values on-the-fly.
    """
    while n > 0:
        yield n
        n -= 1

# Generator functions are memory efficient
for num in countdown(5):
    print(num, end=" ")  # Output: 5 4 3 2 1
print()


def fibonacci_generator(n):
    """
    Generator for Fibonacci sequence - more memory efficient than regular function.
    """
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

# Generate first 10 Fibonacci numbers
fib_nums = list(fibonacci_generator(10))
print(fib_nums)  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


# ============================================================================
# SUMMARY
# ============================================================================
"""
KEY CONCEPTS TO REMEMBER:

1. Functions are defined with 'def' keyword
2. Parameters receive values, arguments are values passed to functions
3. Use 'return' to send values back to the caller
4. Default parameters allow optional arguments
5. *args collects extra positional arguments into a tuple
6. **kwargs collects extra keyword arguments into a dictionary
7. Lambda functions are anonymous, one-line functions
8. Recursive functions call themselves (need base case!)
9. Variables have scope (local vs global)
10. Docstrings document your functions
11. Type hints improve code clarity
12. Functions are first-class objects in Python
13. Nested functions can create closures
14. Generator functions use 'yield' for memory efficiency

PRACTICE TIPS:
- Start with simple functions and gradually add complexity
- Always write docstrings for your functions
- Use meaningful function and parameter names
- Test your functions with different inputs
- Practice by solving problems using functions
"""

