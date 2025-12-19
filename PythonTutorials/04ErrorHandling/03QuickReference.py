"""
================================================================================
ERROR HANDLING QUICK REFERENCE - Cheat Sheet
================================================================================
Copy-paste ready code snippets for common error handling patterns
"""

# ============================================================================
# PATTERN 1: Basic Try-Except
# ============================================================================

try:
    # Your code here
    result = risky_operation()
except SomeError:
    # Handle error
    print("Error occurred")

# ============================================================================
# PATTERN 2: Multiple Exception Types
# ============================================================================

try:
    result = operation()
except (TypeError, ValueError) as e:
    print(f"Error: {e}")
except ZeroDivisionError:
    print("Cannot divide by zero")

# ============================================================================
# PATTERN 3: Try-Except-Else-Finally
# ============================================================================

try:
    result = operation()
except SomeError:
    print("Error handled")
else:
    # Runs only if NO exception
    print("Success!")
finally:
    # ALWAYS runs
    cleanup()

# ============================================================================
# PATTERN 4: File Operations (Best Practice)
# ============================================================================

try:
    with open('file.txt', 'r') as f:
        content = f.read()
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")

# ============================================================================
# PATTERN 5: Raising Exceptions
# ============================================================================

if invalid_condition:
    raise ValueError("Descriptive error message")

# ============================================================================
# PATTERN 6: Custom Exception
# ============================================================================

class CustomError(Exception):
    """Custom exception for your domain"""
    pass

# Usage:
raise CustomError("Custom error message")

# ============================================================================
# PATTERN 7: Input Validation
# ============================================================================

def get_number():
    while True:
        try:
            num = int(input("Enter a number: "))
            return num
        except ValueError:
            print("Invalid input. Please enter a number.")

# ============================================================================
# PATTERN 8: Dictionary Safe Access
# ============================================================================

# Method 1: Try-Except
try:
    value = my_dict['key']
except KeyError:
    value = default_value

# Method 2: get() method (simpler)
value = my_dict.get('key', default_value)

# ============================================================================
# PATTERN 9: List Safe Access
# ============================================================================

try:
    item = my_list[index]
except IndexError:
    item = None  # or handle appropriately

# ============================================================================
# PATTERN 10: Function with Error Handling Wrapper
# ============================================================================

def safe_operation(func, *args, **kwargs):
    """Wrapper function for safe execution"""
    try:
        return func(*args, **kwargs)
    except Exception as e:
        print(f"Error in {func.__name__}: {e}")
        return None

# Usage:
result = safe_operation(risky_function, arg1, arg2)

# ============================================================================
# COMMON EXCEPTIONS QUICK REFERENCE
# ============================================================================

"""
ValueError        - Wrong value type (int("abc"))
TypeError         - Wrong type operation ("5" + 3)
KeyError          - Dictionary key not found
IndexError        - List index out of range
FileNotFoundError - File doesn't exist
PermissionError   - No permission to access file
ZeroDivisionError - Division by zero
AttributeError    - Object doesn't have attribute
ImportError       - Module import failed
"""

# ============================================================================
# PRODUCTION-READY PATTERN (with logging)
# ============================================================================

import logging

logging.basicConfig(level=logging.ERROR)

try:
    result = critical_operation()
except Exception as e:
    logging.error(f"Error in critical_operation: {e}", exc_info=True)
    # Handle error appropriately
    result = None

print("\n✅ Quick Reference loaded!")
print("💡 Copy-paste these patterns into your projects!")
