"""
PYTHON OBJECT-ORIENTED PROGRAMMING (OOP) TUTORIAL
==================================================
This file contains comprehensive examples of OOP concepts in Python with detailed comments.
Learn step by step from basic to advanced concepts.
"""

# ============================================================================
# 1. BASIC CLASS AND OBJECT
# ============================================================================

class Car:
    """
    A class is a blueprint for creating objects.
    It defines attributes (data) and methods (functions) that objects will have.
    """
    
    def __init__(self, make, model, year):
        """
        __init__ is a special method called constructor.
        It's automatically called when you create an object (instance) of the class.
        'self' refers to the instance of the class (the object being created).
        """
        self.make = make      # Instance attribute
        self.model = model    # Instance attribute
        self.year = year      # Instance attribute
    
    def full_name(self):
        """
        Instance method - a function that belongs to an object.
        It can access and modify the object's attributes using 'self'.
        """
        return f"{self.make} {self.model} {self.year}"

# Creating objects (instances) of the Car class
my_car = Car("Toyota", "Corolla", 2020)
your_car = Car("Honda", "Civic", 2021)

# Accessing attributes
print(f"My car: {my_car.make} {my_car.model}")  # Output: My car: Toyota Corolla
print(f"Your car: {your_car.full_name()}")      # Output: Your car: Honda Civic 2021

# Each object has its own separate copy of attributes
print(f"Year difference: {your_car.year - my_car.year}")  # Output: Year difference: 1


# ============================================================================
# 2. CLASS METHOD AND SELF
# ============================================================================

class Student:
    """
    Understanding 'self' and instance methods.
    'self' is a reference to the current instance of the class.
    """
    
    def __init__(self, name, age, grade):
        """
        Constructor initializes instance variables.
        These are unique to each object.
        """
        self.name = name
        self.age = age
        self.grade = grade
    
    def introduce(self):
        """
        Instance method - 'self' allows access to instance attributes.
        When you call student1.introduce(), Python automatically passes
        student1 as the 'self' parameter.
        """
        return f"Hi, I'm {self.name}, {self.age} years old, in grade {self.grade}"
    
    def have_birthday(self):
        """
        Instance methods can modify instance attributes.
        """
        self.age += 1
        return f"{self.name} is now {self.age} years old!"
    
    def get_info(self):
        """
        Another instance method demonstrating self usage.
        """
        return {
            "name": self.name,
            "age": self.age,
            "grade": self.grade
        }

# Creating student objects
student1 = Student("Alice", 15, 10)
student2 = Student("Bob", 16, 11)

print(student1.introduce())  # Output: Hi, I'm Alice, 15 years old, in grade 10
print(student2.introduce())  # Output: Hi, I'm Bob, 16 years old, in grade 11

# Modifying object state
print(student1.have_birthday())  # Output: Alice is now 16 years old!
print(student1.get_info())      # Output: {'name': 'Alice', 'age': 16, 'grade': 10}


# ============================================================================
# 3. INHERITANCE
# ============================================================================

class Animal:
    """
    Parent class (base class or superclass).
    Contains common attributes and methods for all animals.
    """
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        """
        This method can be overridden in child classes.
        """
        return "Some generic animal sound"
    
    def info(self):
        return f"{self.name} is a {self.species}"

class Dog(Animal):
    """
    Child class (derived class or subclass).
    Inherits from Animal class.
    Syntax: class ChildClass(ParentClass):
    """
    
    def __init__(self, name, breed):
        """
        Calling parent class constructor using super().
        super() gives access to parent class methods and attributes.
        """
        super().__init__(name, "Dog")  # Call parent's __init__
        self.breed = breed
    
    def make_sound(self):
        """
        Method overriding - child class provides its own implementation.
        This overrides the parent's make_sound() method.
        """
        return "Woof! Woof!"
    
    def fetch(self):
        """
        Child class can have its own unique methods.
        """
        return f"{self.name} is fetching the ball!"

class Cat(Animal):
    """
    Another child class inheriting from Animal.
    """
    
    def __init__(self, name, color):
        super().__init__(name, "Cat")
        self.color = color
    
    def make_sound(self):
        return "Meow! Meow!"
    
    def climb_tree(self):
        return f"{self.name} is climbing a tree!"

# Creating objects
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Orange")

print(dog.info())           # Output: Buddy is a Dog (inherited method)
print(dog.make_sound())     # Output: Woof! Woof! (overridden method)
print(dog.fetch())          # Output: Buddy is fetching the ball! (unique method)

print(cat.info())           # Output: Whiskers is a Cat
print(cat.make_sound())     # Output: Meow! Meow!
print(cat.climb_tree())     # Output: Whiskers is climbing a tree!


# ============================================================================
# 4. ENCAPSULATION
# ============================================================================

class BankAccount:
    """
    Encapsulation means hiding internal details and protecting data.
    In Python, we use naming conventions:
    - Public: normal naming (self.balance)
    - Protected: single underscore prefix (self._balance) - convention only
    - Private: double underscore prefix (self.__balance) - name mangling
    """
    
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.__balance = initial_balance  # Private attribute (double underscore)
        self._transaction_count = 0       # Protected attribute (single underscore)
    
    def deposit(self, amount):
        """
        Public method to deposit money.
        This is the proper way to modify balance (encapsulation).
        """
        if amount > 0:
            self.__balance += amount
            self._transaction_count += 1
            return f"Deposited ${amount}. New balance: ${self.__balance}"
        return "Invalid deposit amount"
    
    def withdraw(self, amount):
        """
        Public method to withdraw money with validation.
        """
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            self._transaction_count += 1
            return f"Withdrew ${amount}. New balance: ${self.__balance}"
        return "Invalid withdrawal amount or insufficient funds"
    
    def get_balance(self):
        """
        Public method to access balance (getter).
        This provides controlled access to private data.
        """
        return self.__balance
    
    def get_transaction_count(self):
        """
        Getter for protected attribute.
        """
        return self._transaction_count

# Creating account
account = BankAccount("12345", 1000)

# Public methods work fine
print(account.deposit(500))   # Output: Deposited $500. New balance: $1500
print(account.withdraw(200))  # Output: Withdrew $200. New balance: $1300
print(f"Balance: ${account.get_balance()}")  # Output: Balance: $1300

# Direct access to private attribute (not recommended, but Python allows with name mangling)
# print(account.__balance)  # This would cause AttributeError
# But you can access it with name mangling (not recommended):
# print(account._BankAccount__balance)  # Works but violates encapsulation

# Protected attribute can be accessed (but shouldn't be)
print(f"Transactions: {account._transaction_count}")  # Works, but not recommended


# ============================================================================
# 5. PROPERTY DECORATORS (GETTERS AND SETTERS)
# ============================================================================

class Temperature:
    """
    Property decorators provide a Pythonic way to use getters and setters.
    They allow you to access methods like attributes.
    """
    
    def __init__(self, celsius=0):
        self._celsius = celsius  # Protected attribute
    
    @property
    def celsius(self):
        """
        Getter method using @property decorator.
        Now you can access it like: temp.celsius (not temp.celsius())
        """
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """
        Setter method using @celsius.setter decorator.
        Now you can set it like: temp.celsius = 25 (not temp.celsius(25))
        """
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero!")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        """
        Computed property - calculates fahrenheit from celsius.
        """
        return (self._celsius * 9/5) + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        """
        Setter that converts fahrenheit to celsius.
        """
        self._celsius = (value - 32) * 5/9

# Using properties
temp = Temperature(25)
print(f"Celsius: {temp.celsius}")        # Output: Celsius: 25 (accessed like attribute)
print(f"Fahrenheit: {temp.fahrenheit}")   # Output: Fahrenheit: 77.0

temp.celsius = 30  # Setter is called automatically
print(f"New Celsius: {temp.celsius}")    # Output: New Celsius: 30

temp.fahrenheit = 100  # Setter converts to celsius
print(f"Celsius from 100°F: {temp.celsius:.2f}")  # Output: Celsius from 100°F: 37.78


class Person:
    """
    Another example of properties with validation.
    """
    
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not value or not isinstance(value, str):
            raise ValueError("Name must be a non-empty string")
        self._name = value
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Age must be a non-negative integer")
        self._age = value

person = Person("Alice", 25)
print(f"{person.name} is {person.age} years old")  # Output: Alice is 25 years old

person.age = 26  # Setter validates and sets
print(f"New age: {person.age}")  # Output: New age: 26


# ============================================================================
# 6. CLASS VARIABLES
# ============================================================================

class Employee:
    """
    Class variables are shared by all instances of the class.
    Instance variables are unique to each instance.
    """
    
    # Class variable (shared by all instances)
    company_name = "Tech Corp"
    employee_count = 0
    
    def __init__(self, name, position, salary):
        # Instance variables (unique to each instance)
        self.name = name
        self.position = position
        self.salary = salary
        
        # Increment class variable when new employee is created
        Employee.employee_count += 1
    
    def display_info(self):
        """
        Can access both class and instance variables.
        """
        return f"{self.name} works as {self.position} at {Employee.company_name} earning ${self.salary}"
    
    @classmethod
    def get_employee_count(cls):
        """
        Class method - works with class variables, not instance variables.
        'cls' refers to the class itself (like 'self' refers to instance).
        """
        return f"Total employees: {cls.employee_count}"
    
    @classmethod
    def change_company_name(cls, new_name):
        """
        Class method to modify class variable.
        """
        cls.company_name = new_name
        return f"Company name changed to {new_name}"

# Creating employees
emp1 = Employee("Alice", "Developer", 80000)
emp2 = Employee("Bob", "Designer", 70000)
emp3 = Employee("Charlie", "Manager", 90000)

# All instances share the same class variable
print(emp1.company_name)  # Output: Tech Corp
print(emp2.company_name)  # Output: Tech Corp
print(emp3.company_name)  # Output: Tech Corp

# Instance variables are unique
print(emp1.name)  # Output: Alice
print(emp2.name)  # Output: Bob

# Accessing class method
print(Employee.get_employee_count())  # Output: Total employees: 3

# Changing class variable affects all instances
Employee.change_company_name("New Tech Corp")
print(emp1.company_name)  # Output: New Tech Corp
print(emp2.company_name)  # Output: New Tech Corp

# Accessing via instance also works
print(emp1.get_employee_count())  # Output: Total employees: 3


# ============================================================================
# 7. STATIC METHOD
# ============================================================================

class MathUtils:
    """
    Static methods don't need 'self' or 'cls'.
    They are utility functions that belong to the class but don't need
    access to instance or class data.
    """
    
    @staticmethod
    def add(a, b):
        """
        Static method - no 'self' or 'cls' parameter.
        Can be called on the class or an instance.
        """
        return a + b
    
    @staticmethod
    def multiply(a, b):
        return a * b
    
    @staticmethod
    def is_even(number):
        return number % 2 == 0
    
    @staticmethod
    def factorial(n):
        if n <= 1:
            return 1
        return n * MathUtils.factorial(n - 1)

# Calling static methods (no need to create an object)
result1 = MathUtils.add(5, 3)
print(f"5 + 3 = {result1}")  # Output: 5 + 3 = 8

result2 = MathUtils.multiply(4, 7)
print(f"4 * 7 = {result2}")  # Output: 4 * 7 = 28

print(f"Is 10 even? {MathUtils.is_even(10)}")  # Output: Is 10 even? True
print(f"5! = {MathUtils.factorial(5)}")       # Output: 5! = 120

# Can also call on instance (but not necessary)
utils = MathUtils()
print(utils.add(2, 2))  # Output: 4


class DateUtils:
    """
    Another example of static methods for utility functions.
    """
    
    @staticmethod
    def is_leap_year(year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    
    @staticmethod
    def days_in_month(month, year):
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if month == 2 and DateUtils.is_leap_year(year):
            return 29
        return days[month - 1]

print(f"2024 is leap year: {DateUtils.is_leap_year(2024)}")  # Output: 2024 is leap year: True
print(f"Days in Feb 2024: {DateUtils.days_in_month(2, 2024)}")  # Output: Days in Feb 2024: 29


# ============================================================================
# 8. CLASS INHERITANCE AND isinstance() FUNCTION
# ============================================================================

class Vehicle:
    """
    Base class for all vehicles.
    """
    
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def start(self):
        return f"{self.brand} {self.model} is starting..."

class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors
    
    def honk(self):
        return "Beep! Beep!"

class Motorcycle(Vehicle):
    def __init__(self, brand, model, engine_cc):
        super().__init__(brand, model)
        self.engine_cc = engine_cc
    
    def wheelie(self):
        return "Doing a wheelie!"

class Truck(Vehicle):
    def __init__(self, brand, model, load_capacity):
        super().__init__(brand, model)
        self.load_capacity = load_capacity

# Creating objects
car = Car("Toyota", "Camry", 4)
motorcycle = Motorcycle("Yamaha", "R1", 1000)
truck = Truck("Ford", "F-150", "5000 lbs")

# isinstance() function checks if an object is an instance of a class
print(isinstance(car, Car))         # Output: True
print(isinstance(car, Vehicle))    # Output: True (inheritance)
print(isinstance(car, Motorcycle)) # Output: False

print(isinstance(motorcycle, Vehicle))  # Output: True
print(isinstance(truck, Vehicle))       # Output: True

# isinstance() also works with multiple types
print(isinstance(car, (Car, Motorcycle, Truck)))  # Output: True

# Checking type hierarchy
vehicles = [car, motorcycle, truck]
for vehicle in vehicles:
    print(f"{vehicle.brand} is Vehicle: {isinstance(vehicle, Vehicle)}")
# Output:
# Toyota is Vehicle: True
# Yamaha is Vehicle: True
# Ford is Vehicle: True


# ============================================================================
# 9. MULTIPLE INHERITANCE
# ============================================================================

class Flyable:
    """
    First parent class (mixin).
    """
    
    def fly(self):
        return "Flying through the air!"
    
    def land(self):
        return "Landing safely..."

class Swimmable:
    """
    Second parent class (mixin).
    """
    
    def swim(self):
        return "Swimming in water!"
    
    def dive(self):
        return "Diving deep..."

class Duck(Animal, Flyable, Swimmable):
    """
    Multiple inheritance - inherits from multiple parent classes.
    Duck inherits from Animal, Flyable, and Swimmable.
    """
    
    def __init__(self, name):
        super().__init__(name, "Duck")
    
    def make_sound(self):
        return "Quack! Quack!"
    
    def display_abilities(self):
        """
        Can use methods from all parent classes.
        """
        abilities = [
            self.make_sound(),
            self.fly(),
            self.swim(),
            self.dive()
        ]
        return abilities

duck = Duck("Donald")
print(duck.info())  # Output: Donald is a Duck (from Animal)
print(duck.make_sound())  # Output: Quack! Quack!
print(duck.fly())  # Output: Flying through the air! (from Flyable)
print(duck.swim())  # Output: Swimming in water! (from Swimmable)

abilities = duck.display_abilities()
for ability in abilities:
    print(f"  - {ability}")


class Electric:
    """
    Another mixin class.
    """
    
    def charge(self):
        return "Charging battery..."
    
    def get_battery_level(self):
        return "Battery: 80%"

class Hybrid:
    """
    Another mixin class.
    """
    
    def use_gas(self):
        return "Using gasoline..."
    
    def use_electric(self):
        return "Using electric mode..."

class HybridCar(Car, Electric, Hybrid):
    """
    Multiple inheritance example with Car and two mixins.
    """
    
    def __init__(self, brand, model, doors, battery_capacity):
        Car.__init__(self, brand, model, doors)
        self.battery_capacity = battery_capacity
    
    def display_modes(self):
        return [
            self.use_gas(),
            self.use_electric(),
            self.charge()
        ]

hybrid = HybridCar("Toyota", "Prius", 4, "50 kWh")
print(hybrid.full_name())  # Output: Toyota Prius 2020 (from Car)
print(hybrid.honk())       # Output: Beep! Beep! (from Car)
print(hybrid.charge())     # Output: Charging battery... (from Electric)

modes = hybrid.display_modes()
for mode in modes:
    print(f"  - {mode}")


# ============================================================================
# 10. METHOD RESOLUTION ORDER (MRO)
# ============================================================================

class A:
    def method(self):
        return "Method from A"

class B(A):
    def method(self):
        return "Method from B"

class C(A):
    def method(self):
        return "Method from C"

class D(B, C):
    """
    Multiple inheritance - which method is called?
    Python uses Method Resolution Order (MRO) to determine this.
    """
    pass

d = D()
print(d.method())  # Output: Method from B (B comes before C in inheritance)

# Check MRO
print(D.__mro__)  # Shows the order: D -> B -> C -> A -> object
# Output: (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)


# ============================================================================
# 11. SPECIAL METHODS (MAGIC METHODS / DUNDER METHODS)
# ============================================================================

class Book:
    """
    Special methods (dunder methods) allow you to define how objects behave
    with built-in operations like +, ==, <, str(), len(), etc.
    """
    
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        """
        Called by str() and print().
        Should return a human-readable string.
        """
        return f"'{self.title}' by {self.author}"
    
    def __repr__(self):
        """
        Called by repr().
        Should return an unambiguous string representation.
        """
        return f"Book('{self.title}', '{self.author}', {self.pages})"
    
    def __len__(self):
        """
        Called by len().
        """
        return self.pages
    
    def __eq__(self, other):
        """
        Called by == operator.
        """
        if isinstance(other, Book):
            return self.title == other.title and self.author == other.author
        return False
    
    def __lt__(self, other):
        """
        Called by < operator (less than).
        """
        if isinstance(other, Book):
            return self.pages < other.pages
        return NotImplemented
    
    def __add__(self, other):
        """
        Called by + operator.
        """
        if isinstance(other, Book):
            return Book(
                f"{self.title} & {other.title}",
                f"{self.author} & {other.author}",
                self.pages + other.pages
            )
        return NotImplemented

book1 = Book("Python Basics", "John Doe", 300)
book2 = Book("Advanced Python", "Jane Smith", 500)

print(book1)              # Output: 'Python Basics' by John Doe (uses __str__)
print(repr(book1))        # Output: Book('Python Basics', 'John Doe', 300) (uses __repr__)
print(f"Pages: {len(book1)}")  # Output: Pages: 300 (uses __len__)

print(book1 == book2)     # Output: False (uses __eq__)
print(book1 < book2)      # Output: True (uses __lt__)

combined = book1 + book2  # Uses __add__
print(combined)           # Output: 'Python Basics & Advanced Python' by John Doe & Jane Smith


# ============================================================================
# 12. ABSTRACT BASE CLASSES
# ============================================================================

from abc import ABC, abstractmethod

class Shape(ABC):
    """
    Abstract base class - cannot be instantiated directly.
    Forces child classes to implement abstract methods.
    """
    
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def area(self):
        """
        Abstract method - must be implemented by child classes.
        """
        pass
    
    @abstractmethod
    def perimeter(self):
        """
        Another abstract method.
        """
        pass
    
    def display_info(self):
        """
        Regular method - can be used by all child classes.
        """
        return f"{self.name} - Area: {self.area():.2f}, Perimeter: {self.perimeter():.2f}"

class Rectangle(Shape):
    """
    Concrete class - implements all abstract methods.
    """
    
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    """
    Another concrete class.
    """
    
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14159 * self.radius

# shape = Shape("Generic")  # This would raise TypeError - cannot instantiate abstract class

rect = Rectangle(5, 3)
circle = Circle(4)

print(rect.display_info())   # Output: Rectangle - Area: 15.00, Perimeter: 16.00
print(circle.display_info()) # Output: Circle - Area: 50.27, Perimeter: 25.13


# ============================================================================
# 13. COMPOSITION vs INHERITANCE
# ============================================================================

class Engine:
    """
    Composition example - "has-a" relationship.
    """
    
    def __init__(self, horsepower):
        self.horsepower = horsepower
    
    def start(self):
        return f"Engine ({self.horsepower} HP) started!"

class Wheel:
    def __init__(self, size):
        self.size = size
    
    def rotate(self):
        return f"Wheel ({self.size} inches) rotating..."

class VehicleComposition:
    """
    Composition: Vehicle HAS-A Engine and HAS-A Wheel(s).
    This is often preferred over inheritance for "has-a" relationships.
    """
    
    def __init__(self, brand, engine_hp, wheel_size):
        self.brand = brand
        self.engine = Engine(engine_hp)  # Composition
        self.wheels = [Wheel(wheel_size) for _ in range(4)]  # Composition
    
    def start(self):
        return self.engine.start()
    
    def drive(self):
        return f"{self.brand} is driving with {len(self.wheels)} wheels!"

car_comp = VehicleComposition("BMW", 300, 18)
print(car_comp.start())   # Output: Engine (300 HP) started!
print(car_comp.drive())   # Output: BMW is driving with 4 wheels!


# ============================================================================
# 14. PRACTICAL EXAMPLE: LIBRARY MANAGEMENT SYSTEM
# ============================================================================

class LibraryItem:
    """
    Practical example combining multiple OOP concepts.
    """
    
    total_items = 0  # Class variable
    
    def __init__(self, title, item_id):
        self.title = title
        self._item_id = item_id  # Protected
        self.__is_available = True  # Private
        LibraryItem.total_items += 1
    
    @property
    def item_id(self):
        return self._item_id
    
    @property
    def is_available(self):
        return self.__is_available
    
    def borrow(self):
        if self.__is_available:
            self.__is_available = False
            return f"'{self.title}' has been borrowed."
        return f"'{self.title}' is not available."
    
    def return_item(self):
        self.__is_available = True
        return f"'{self.title}' has been returned."
    
    @classmethod
    def get_total_items(cls):
        return cls.total_items
    
    def __str__(self):
        status = "Available" if self.__is_available else "Borrowed"
        return f"{self.title} (ID: {self._item_id}) - {status}"

class Book(LibraryItem):
    def __init__(self, title, item_id, author, pages):
        super().__init__(title, item_id)
        self.author = author
        self.pages = pages
    
    def __str__(self):
        base = super().__str__()
        return f"{base} - {self.author} ({self.pages} pages)"

class DVD(LibraryItem):
    def __init__(self, title, item_id, director, duration):
        super().__init__(title, item_id)
        self.director = director
        self.duration = duration
    
    def __str__(self):
        base = super().__str__()
        return f"{base} - {self.director} ({self.duration} min)"

# Using the library system
book1 = Book("Python Guide", "B001", "John Doe", 400)
dvd1 = DVD("Python Tutorial", "D001", "Jane Smith", 120)

print(book1)
print(dvd1)

print(book1.borrow())
print(book1)
print(book1.return_item())

print(f"Total library items: {LibraryItem.get_total_items()}")


# ============================================================================
# SUMMARY
# ============================================================================
"""
KEY OOP CONCEPTS IN PYTHON:

1. CLASS AND OBJECT
   - Class is a blueprint, object is an instance
   - Use __init__() constructor to initialize objects
   - 'self' refers to the instance

2. INHERITANCE
   - Child classes inherit from parent classes
   - Use super() to call parent class methods
   - Method overriding allows child classes to customize behavior

3. ENCAPSULATION
   - Public: normal attributes
   - Protected: _single_underscore (convention)
   - Private: __double_underscore (name mangling)
   - Use getters/setters for controlled access

4. POLYMORPHISM
   - Same interface, different implementations
   - Method overriding enables polymorphism
   - isinstance() checks object types

5. CLASS VARIABLES
   - Shared by all instances
   - Use @classmethod for class-level operations
   - 'cls' refers to the class

6. STATIC METHODS
   - Don't need 'self' or 'cls'
   - Utility functions belonging to class
   - Use @staticmethod decorator

7. PROPERTY DECORATORS
   - @property for getters
   - @attribute.setter for setters
   - Access methods like attributes

8. MULTIPLE INHERITANCE
   - Class can inherit from multiple parents
   - Method Resolution Order (MRO) determines method lookup
   - Useful for mixins

9. SPECIAL METHODS
   - __str__, __repr__, __len__, __eq__, __add__, etc.
   - Define object behavior with operators

10. ABSTRACT CLASSES
    - Cannot be instantiated
    - Force implementation of abstract methods
    - Use ABC and @abstractmethod

BEST PRACTICES:
- Use meaningful class and method names
- Follow naming conventions (CamelCase for classes)
- Document with docstrings
- Prefer composition over inheritance when appropriate
- Use properties for computed attributes
- Keep methods focused and single-purpose
- Use type hints for better code clarity
"""
