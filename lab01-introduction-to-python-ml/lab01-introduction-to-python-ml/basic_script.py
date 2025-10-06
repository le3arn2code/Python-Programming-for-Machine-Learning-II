# This is a basic Python script for learning purposes

# Print a welcome message
print("Hello, welcome to Python for Machine Learning!")

# Variables and basic data types
x = 10          # Integer
y = 5.5         # Float
name = "John"   # String

print(f"Integer value: {x}, Float value: {y}, Name: {name}")

# Perform arithmetic operations
result = x + y
print(f"Sum of {x} and {y} is {result}")

# List (array)
numbers = [1, 2, 3, 4, 5]
print(f"List of numbers: {numbers}")

# Loop through the list
for number in numbers:
    print(f"Number: {number}")

# If-else condition
if x > y:
    print(f"{x} is greater than {y}")
else:
    print(f"{x} is not greater than {y}")

# -------- Extra exploration --------
# Tuple (immutable list)
my_tuple = (1, 2, 3)
print(f"Tuple: {my_tuple}")

# Dictionary (key-value pairs)
my_dict = {'name': 'Alice', 'age': 25}
print(f"Dictionary: {my_dict}")

# While loop
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1

# Functions
def greet(person):
    return f"Hello, {person}!"

print(greet("Alice"))
