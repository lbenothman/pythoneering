"""
Walrus Operator (:=) Examples
Python 3.8+ assignment expressions
"""

# Example 1: Avoid duplicate function calls
def get_data():
    """Simulate fetching data"""
    print("Fetching data...")
    return {"status": "success", "items": [1, 2, 3]}

def process(data):
    """Process the data"""
    print(f"Processing: {data}")

# Instead of:
data = get_data()
if data:
    process(data)

# Use:
if (data := get_data()):
    process(data)


# Example 2: List comprehensions with filtering
def process_expensive(x):
    """Simulate an expensive operation"""
    return x * 2

numbers = [1, 2, 3, 4, 5]

# Instead of (process_expensive called twice per item):
results = [process_expensive(n) for n in numbers if process_expensive(n) > 5]
print(f"Without walrus: {results}")

# Use (process_expensive called only once per item):
results = [result for n in numbers if (result := process_expensive(n)) > 5]
print(f"With walrus: {results}")


# Example 3: Regex matching
import re

# Instead of:
text = "Email: john@example.com"
match = re.search(r'(\w+)@(\w+\.\w+)', text)
if match:
    print(f"Username: {match.group(1)}, Domain: {match.group(2)}")

# Use:
if (match := re.search(r'(\w+)@(\w+\.\w+)', text)):
    print(f"Username: {match.group(1)}, Domain: {match.group(2)}")


# Example 4: Computing values in conditions
some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# Instead of:
length = len(some_list)
if length > 10:
    print(f"List is long: {length} items")

# Use:
if (length := len(some_list)) > 10:
    print(f"List is long: {length} items")


# Example 5: Dictionary operations
data_dict = {"name": "Python", "version": "3.12"}

# Check if key exists and use the value
if (value := data_dict.get("name")):
    print(f"Found: {value}")


# Example 6: While loops with conditions
counter = 0

# Compute and check in the same expression
while (counter := counter + 1) <= 5:
    print(f"Count: {counter}")


print("\nAll walrus operator examples demonstrated!")