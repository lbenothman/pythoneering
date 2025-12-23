"""
functools.partial - Pre-fill Function Arguments
"""

from functools import partial
from operator import mul


# Example 1: Reduce Repetitive Function Calls
print("Example 1: Reduce Repetitive Function Calls")
print("=" * 60)


def log(level, message):
    print(f"[{level}] {message}")


# Without partial - repetitive
print("\nWithout partial:")
log("ERROR", "Database connection failed")
log("ERROR", "Invalid credentials")
log("ERROR", "Timeout occurred")

# With partial - cleaner
print("\nWith partial:")
log_error = partial(log, "ERROR")
log_info = partial(log, "INFO")

log_error("Database connection failed")
log_info("User logged in successfully")
log_error("Invalid credentials")


# Example 2: Cleaner Map Operations
print("\n\nExample 2: Cleaner Map Operations")
print("=" * 60)

hex_numbers = ['ff', 'a0', '1b', '3c']
print(f"\nInput: {hex_numbers}")

# Without partial - need lambda
result_lambda = list(map(lambda x: int(x, base=16), hex_numbers))
print(f"With lambda: {result_lambda}")

# With partial - cleaner and reusable
parse_hex = partial(int, base=16)
result_partial = list(map(parse_hex, hex_numbers))
print(f"With partial: {result_partial}")

# Another example: multiply numbers
numbers = [1, 2, 3, 4, 5]
print(f"\nMultiplying {numbers} by 10:")

multiply_by_10 = partial(mul, 10)
result = list(map(multiply_by_10, numbers))
print(f"Result: {result}")