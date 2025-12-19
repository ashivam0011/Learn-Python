"""
================================================================================
ERROR HANDLING IN PYTHON - Complete Guide for Junior Developers
================================================================================

WHY ERROR HANDLING?
------------------
- Prevents program crashes
- Provides user-friendly error messages
- Helps debug issues
- Makes code production-ready

KEY CONCEPT: Python raises "exceptions" when errors occur. We "catch" them.
"""

# ============================================================================
# 1. BASIC TRY-EXCEPT BLOCK
# ============================================================================

print("\n" + "="*70)
print("1. BASIC TRY-EXCEPT BLOCK")
print("="*70)

# Without error handling (BAD - crashes the program)
# result = 10 / 0  # ZeroDivisionError: division by zero

# With error handling (GOOD - handles gracefully)
try:
    result = 10 / 0
except ZeroDivisionError:
    print("⚠️  Cannot divide by zero!")

# NOTE: The code after try-except continues running even if error occurs
print("Program continues...")

# ============================================================================
# 2. CATCHING SPECIFIC EXCEPTIONS
# ============================================================================

print("\n" + "="*70)
print("2. CATCHING SPECIFIC EXCEPTIONS")
print("="*70)

def divide_numbers(a, b):
    """Divide two numbers with error handling"""
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero!"
    except TypeError:
        return "Error: Both values must be numbers!"

# Test cases
print(divide_numbers(10, 2))      # Works fine: 5.0
print(divide_numbers(10, 0))      # Catches ZeroDivisionError
print(divide_numbers(10, "abc"))  # Catches TypeError

# ============================================================================
# 3. CATCHING MULTIPLE EXCEPTIONS
# ============================================================================

print("\n" + "="*70)
print("3. CATCHING MULTIPLE EXCEPTIONS")
print("="*70)

def safe_divide(a, b):
    """Handle multiple error types"""
    try:
        result = a / b
        return f"Result: {result}"
    except (ZeroDivisionError, TypeError) as e:
        # 'as e' captures the error message
        return f"Error occurred: {type(e).__name__} - {str(e)}"

print(safe_divide(10, 0))
print(safe_divide(10, "abc"))

# ============================================================================
# 4. ELSE BLOCK (runs when NO exception occurs)
# ============================================================================

print("\n" + "="*70)
print("4. ELSE BLOCK")
print("="*70)

def process_number(num):
    """Demonstrate else block"""
    try:
        result = 100 / num
    except ZeroDivisionError:
        print("⚠️  Division by zero!")
    else:
        # Only runs if NO exception occurred
        print(f"✅ Success! Result: {result}")

process_number(5)   # Prints success message
process_number(0)   # Prints error message

# ============================================================================
# 5. FINALLY BLOCK (ALWAYS runs)
# ============================================================================

print("\n" + "="*70)
print("5. FINALLY BLOCK - Always Executes")
print("="*70)

def read_file_safely(filename):
    """Demonstrate finally block - perfect for cleanup"""
    file = None
    try:
        file = open(filename, 'r')
        content = file.read()
        return content
    except FileNotFoundError:
        return "File not found!"
    finally:
        # ALWAYS runs - even if error occurs
        if file:
            file.close()
            print("🔒 File closed (cleanup done)")

# NOTE: In real projects, use 'with' statement (see below)

# ============================================================================
# 6. COMMON EXCEPTION TYPES (You'll see these often)
# ============================================================================

print("\n" + "="*70)
print("6. COMMON EXCEPTION TYPES")
print("="*70)

# ValueError - Wrong value type
try:
    int("abc")
except ValueError as e:
    print(f"ValueError: {e}")

# KeyError - Dictionary key doesn't exist
try:
    data = {"name": "Shivam"}
    print(data["age"])
except KeyError as e:
    print(f"KeyError: Key '{e}' not found")

# IndexError - List index out of range
try:
    numbers = [1, 2, 3]
    print(numbers[10])
except IndexError as e:
    print(f"IndexError: {e}")

# AttributeError - Object doesn't have attribute
try:
    "hello".some_method()
except AttributeError as e:
    print(f"AttributeError: {e}")

# ============================================================================
# 7. BEST PRACTICES - Context Manager (with statement)
# ============================================================================

print("\n" + "="*70)
print("7. BEST PRACTICE - Using 'with' Statement")
print("="*70)

# OLD WAY (manual cleanup)
# file = open('data.txt', 'r')
# content = file.read()
# file.close()  # Easy to forget!

# NEW WAY (automatic cleanup - RECOMMENDED)
def read_file_better(filename):
    """Best practice: 'with' automatically closes file"""
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "File not found!"

# ============================================================================
# 8. RAISING EXCEPTIONS (Creating your own errors)
# ============================================================================

print("\n" + "="*70)
print("8. RAISING EXCEPTIONS")
print("="*70)

def validate_age(age):
    """Validate age and raise error if invalid"""
    if age < 0:
        raise ValueError("Age cannot be negative!")
    if age > 150:
        raise ValueError("Age seems unrealistic!")
    return f"✅ Valid age: {age}"

try:
    print(validate_age(25))
    print(validate_age(-5))  # Raises ValueError
except ValueError as e:
    print(f"❌ {e}")

# ============================================================================
# 9. CUSTOM EXCEPTIONS (Create your own exception classes)
# ============================================================================

print("\n" + "="*70)
print("9. CUSTOM EXCEPTIONS")
print("="*70)

class InsufficientFundsError(Exception):
    """Custom exception for banking operations"""
    pass

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(
                f"Insufficient funds! Balance: ${self.balance}, Requested: ${amount}"
            )
        self.balance -= amount
        return f"Withdrew ${amount}. New balance: ${self.balance}"

# Usage
account = BankAccount(100)
try:
    print(account.withdraw(50))
    print(account.withdraw(100))  # Raises custom exception
except InsufficientFundsError as e:
    print(f"❌ {e}")

# ============================================================================
# 10. REAL-WORLD EXAMPLE - API Call with Error Handling
# ============================================================================

print("\n" + "="*70)
print("10. REAL-WORLD EXAMPLE - API Call")
print("="*70)

import json

def parse_user_data(data_string):
    """Parse JSON user data with comprehensive error handling"""
    try:
        data = json.loads(data_string)
        
        # Validate required fields
        if "name" not in data:
            raise KeyError("'name' field is required")
        
        if "age" not in data:
            raise KeyError("'age' field is required")
        
        # Validate age is a number
        if not isinstance(data["age"], int):
            raise ValueError("'age' must be an integer")
        
        return f"✅ User: {data['name']}, Age: {data['age']}"
    
    except json.JSONDecodeError:
        return "❌ Invalid JSON format"
    except KeyError as e:
        return f"❌ Missing required field: {e}"
    except ValueError as e:
        return f"❌ Invalid value: {e}"
    except Exception as e:
        # Catch-all for unexpected errors
        return f"❌ Unexpected error: {type(e).__name__} - {str(e)}"

# Test cases
print(parse_user_data('{"name": "Shivam", "age": 21}'))
print(parse_user_data('{"name": "Shivam"}'))  # Missing age
print(parse_user_data('{"name": "Shivam", "age": "twenty"}'))  # Wrong type
print(parse_user_data('invalid json'))  # Invalid JSON

# ============================================================================
# 11. SENIOR DEVELOPER TIPS
# ============================================================================

print("\n" + "="*70)
print("11. SENIOR DEVELOPER TIPS")
print("="*70)

print("""
📝 BEST PRACTICES:

1. ✅ Be SPECIFIC - Catch specific exceptions, not generic Exception
   BAD:  except Exception:  # Too broad
   GOOD: except ValueError:  # Specific

2. ✅ Use 'with' statement for file operations (automatic cleanup)

3. ✅ Log errors in production (use logging module, not print)

4. ✅ Don't suppress errors silently - always handle or log them

5. ✅ Create custom exceptions for your domain logic

6. ✅ Use try-except-else-finally appropriately:
   - try: Code that might fail
   - except: Handle specific errors
   - else: Code that runs on success
   - finally: Cleanup code (always runs)

7. ✅ Validate input early - fail fast principle

8. ✅ Provide meaningful error messages to users
""")

# ============================================================================
# 12. EXERCISES - Practice Time!
# ============================================================================

print("\n" + "="*70)
print("12. EXERCISES - Try These!")
print("="*70)

print("""
EXERCISE 1: Calculator Function
--------------------------------
Create a function 'safe_calculator(a, b, operation)' that:
- Takes two numbers and an operation ('add', 'subtract', 'multiply', 'divide')
- Handles division by zero
- Handles invalid operations
- Returns result or error message

EXERCISE 2: List Processor
---------------------------
Create a function that:
- Takes a list and an index
- Returns the element at that index
- Handles IndexError gracefully
- Handles TypeError if list is not a list

EXERCISE 3: User Input Validator
---------------------------------
Create a function that:
- Takes user input (age as string)
- Converts to integer
- Validates age is between 0-120
- Handles ValueError and custom validation errors

EXERCISE 4: File Reader
-----------------------
Create a function that:
- Reads a file
- Handles FileNotFoundError
- Handles PermissionError
- Returns file content or error message

EXERCISE 5: Custom Exception
-----------------------------
Create a custom exception 'InvalidEmailError'
Use it in a function that validates email format
""")

# ============================================================================
# SOLUTION TEMPLATES (Uncomment and complete)
# ============================================================================

# Exercise 1 Solution Template:
"""
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
            raise ValueError("Invalid operation")
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    except ValueError as e:
        return f"Error: {e}"
"""

print("\n✅ Error Handling Tutorial Complete!")
print("💡 Remember: Good error handling makes your code production-ready!")
