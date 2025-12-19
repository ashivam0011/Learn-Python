"""
================================================================================
ERROR HANDLING EXERCISES - Practice Makes Perfect!
================================================================================

Complete these exercises to master error handling in Python.
Solutions are provided at the bottom (but try yourself first!)
"""

# ============================================================================
# EXERCISE 1: Safe Calculator
# ============================================================================

from asyncio import InvalidStateError
from nt import error


def safe_calculator(a, b, operation):
    match operation:
        case 'add':
            try:
                print( a+b)
            except TypeError:
                print('Invalid Type')
        case 'subtract':
            try:
                print(a-b)
            except TypeError:
                print('Invalid Type')    
        case 'multiply':
            try:
                print( a*b)
            except TypeError:
                print('Invalid Type')
        case 'divide':
            try:
                print(a/b)
            except (ZeroDivisionError,TypeError) as e:
                print(f"Invalid Operands given {type(e).__name__}: {str(e)}")
        case _:
            raise ValueError('Invalid Operation, Please choose valid operation')
    

    # """
    # Create a calculator that handles errors gracefully.
    
    # Args:
    #     a: First number
    #     b: Second number
    #     operation: 'add', 'subtract', 'multiply', 'divide'
    
    # Returns:
    #     Result or error message
    # """
    # TODO: Implement error handling
    # - Handle division by zero
    # - Handle invalid operations
    # - Handle type errors (non-numeric inputs)
    # pass


# Test your function:
print(safe_calculator(10, 5, 'divide'))  # Should return 2.0
print(safe_calculator(10, 0, 'divide'))  # Should handle ZeroDivisionError
print(safe_calculator(10, 5, 'power'))   # Should handle invalid operation


# ============================================================================
# EXERCISE 2: List Element Getter
# ============================================================================

def get_list_element(my_list, index):
    """
    Safely get an element from a list.
    
    Args:
        my_list: A list
        index: Index to access
    
    Returns:
        Element at index or error message
    """
    # TODO: Implement error handling
    # - Handle IndexError (index out of range)
    # - Handle TypeError (not a list)
    pass


# Test your function:
# print(get_list_element([1, 2, 3], 1))     # Should return 2
# print(get_list_element([1, 2, 3], 10))    # Should handle IndexError
# print(get_list_element("not a list", 0))  # Should handle TypeError


# ============================================================================
# EXERCISE 3: Age Validator
# ============================================================================

def validate_age(age_input):
    """
    Validate age input from user.
    
    Args:
        age_input: Age as string (from user input)
    
    Returns:
        Validated age (int) or error message
    """
    # TODO: Implement error handling
    # - Convert string to integer (handle ValueError)
    # - Validate age is between 0-120
    # - Raise custom error for invalid range
    pass


# Test your function:
# print(validate_age("25"))    # Should return 25
# print(validate_age("abc"))   # Should handle ValueError
# print(validate_age("150"))   # Should handle invalid range


# ============================================================================
# EXERCISE 4: File Reader
# ============================================================================

def read_file_safely(filename):
    """
    Read a file with proper error handling.
    
    Args:
        filename: Path to file
    
    Returns:
        File content or error message
    """
    # TODO: Implement error handling
    # - Use 'with' statement (best practice)
    # - Handle FileNotFoundError
    # - Handle PermissionError
    pass


# Test your function:
# print(read_file_safely("existing_file.txt"))
# print(read_file_safely("nonexistent.txt"))  # Should handle FileNotFoundError


# ============================================================================
# EXERCISE 5: Custom Exception - Email Validator
# ============================================================================

# TODO: Create a custom exception class called InvalidEmailError
# class InvalidEmailError(Exception):
#     pass

def validate_email(email):
    """
    Validate email format.
    
    Args:
        email: Email string
    
    Returns:
        True if valid, raises InvalidEmailError if invalid
    """
    # TODO: Implement validation
    # - Check if email contains '@'
    # - Check if email contains '.'
    # - Raise InvalidEmailError if invalid
    # - Return True if valid
    pass


# Test your function:
# try:
#     print(validate_email("shivam@example.com"))  # Should return True
#     print(validate_email("invalid-email"))       # Should raise InvalidEmailError
# except InvalidEmailError as e:
#     print(f"Error: {e}")


# ============================================================================
# EXERCISE 6: Dictionary Safe Access
# ============================================================================

def get_user_info(user_dict, key):
    """
    Safely get value from user dictionary.
    
    Args:
        user_dict: Dictionary with user info
        key: Key to access
    
    Returns:
        Value or helpful error message
    """
    # TODO: Implement error handling
    # - Handle KeyError
    # - Handle TypeError (if not a dict)
    pass


# Test your function:
# user = {"name": "Shivam", "age": 21}
# print(get_user_info(user, "name"))     # Should return "Shivam"
# print(get_user_info(user, "email"))     # Should handle KeyError
# print(get_user_info("not a dict", "name"))  # Should handle TypeError


# ============================================================================
# EXERCISE 7: Number Parser (Advanced)
# ============================================================================

def parse_number(value):
    """
    Parse a number from string, handling multiple formats.
    
    Args:
        value: String that might be a number
    
    Returns:
        Number (int or float) or error message
    """
    # TODO: Implement error handling
    # - Try to convert to int first
    # - If fails, try float
    # - Handle ValueError for both
    # - Handle other unexpected errors
    pass


# Test your function:
# print(parse_number("42"))        # Should return 42 (int)
# print(parse_number("3.14"))      # Should return 3.14 (float)
# print(parse_number("abc"))       # Should handle ValueError


# ============================================================================
# SOLUTIONS (Uncomment to see answers)
# ============================================================================

"""
# SOLUTION 1: Safe Calculator
def safe_calculator(a, b, operation):
    try:
        if operation == 'add':
            return a + b
        elif operation == 'subtract':
            return a - b
        elif operation == 'multiply':
            return a * b
        elif operation == 'divide':
            return a / b
        else:
            raise ValueError(f"Invalid operation: {operation}")
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    except TypeError:
        return "Error: Both values must be numbers"
    except ValueError as e:
        return f"Error: {e}"


# SOLUTION 2: List Element Getter
def get_list_element(my_list, index):
    try:
        return my_list[index]
    except IndexError:
        return f"Error: Index {index} out of range. List has {len(my_list)} elements"
    except TypeError:
        return "Error: First argument must be a list"


# SOLUTION 3: Age Validator
def validate_age(age_input):
    try:
        age = int(age_input)
        if age < 0:
            raise ValueError("Age cannot be negative")
        if age > 120:
            raise ValueError("Age seems unrealistic (max 120)")
        return age
    except ValueError as e:
        if "invalid literal" in str(e).lower():
            return f"Error: '{age_input}' is not a valid number"
        return f"Error: {e}"


# SOLUTION 4: File Reader
def read_file_safely(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return f"Error: File '{filename}' not found"
    except PermissionError:
        return f"Error: Permission denied to read '{filename}'"


# SOLUTION 5: Custom Exception
class InvalidEmailError(Exception):
    pass

def validate_email(email):
    if '@' not in email:
        raise InvalidEmailError(f"Email '{email}' is missing '@' symbol")
    if '.' not in email:
        raise InvalidEmailError(f"Email '{email}' is missing domain extension")
    if email.count('@') > 1:
        raise InvalidEmailError(f"Email '{email}' has multiple '@' symbols")
    return True


# SOLUTION 6: Dictionary Safe Access
def get_user_info(user_dict, key):
    try:
        return user_dict[key]
    except KeyError:
        available_keys = ', '.join(user_dict.keys()) if isinstance(user_dict, dict) else 'N/A'
        return f"Error: Key '{key}' not found. Available keys: {available_keys}"
    except TypeError:
        return "Error: First argument must be a dictionary"


# SOLUTION 7: Number Parser
def parse_number(value):
    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError:
            return f"Error: '{value}' cannot be converted to a number"
"""

print("\n✅ Exercises loaded! Try solving them before checking solutions.")
print("💡 Tip: Run each function with test cases to verify your solution works!")
