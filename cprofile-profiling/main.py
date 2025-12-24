"""
cProfile - Performance Profiling
"""

import cProfile
import pstats
from io import StringIO


# Example 1: Basic Profiling - Find Bottlenecks
print("Example 1: Basic Profiling - Find Bottlenecks")
print("=" * 60)


def fibonacci(n):
    """Inefficient recursive fibonacci."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def calculate_fibonacci_numbers():
    """Calculate multiple fibonacci numbers."""
    results = []
    for i in range(20):
        results.append(fibonacci(i))
    return results


print("\nProfiling fibonacci calculation...")
profiler = cProfile.Profile()
profiler.enable()

# Code to profile
result = calculate_fibonacci_numbers()

profiler.disable()

# Print stats
print(f"\nCalculated {len(result)} fibonacci numbers")
print("\nTop 10 functions by time:")
stats = pstats.Stats(profiler)
stats.sort_stats('cumulative')
stats.print_stats(10)


# Example 2: Membership Testing - List vs Set
print("\n\nExample 2: Membership Testing - List vs Set")
print("=" * 60)


def filter_valid_items_v1(allowed_items, items_to_check):
    """Version 1: Using list (O(n) lookup - slow)."""
    allowed_list = list(allowed_items)
    valid_items = []
    for item in items_to_check:
        if item in allowed_list:  # O(n) lookup for each item
            valid_items.append(item)
    return valid_items


def filter_valid_items_v2(allowed_items, items_to_check):
    """Version 2: Using set (O(1) lookup - fast)."""
    allowed_set = set(allowed_items)
    valid_items = []
    for item in items_to_check:
        if item in allowed_set:  # O(1) lookup for each item
            valid_items.append(item)
    return valid_items


# Create test data - e.g., filtering valid product IDs
allowed_products = list(range(10000))  # 10,000 valid product IDs
products_to_check = list(range(5000, 15000))  # Check 10,000 products

# Profile version 1
print("\nProfiling Version 1 (list membership):")
profiler1 = cProfile.Profile()
profiler1.enable()
result1 = filter_valid_items_v1(allowed_products, products_to_check)
profiler1.disable()

print(f"Filtered to {len(result1)} valid items")
stats1 = pstats.Stats(profiler1)
stats1.sort_stats('cumulative')
stats1.print_stats(5)

# Profile version 2
print("\nProfiling Version 2 (set membership):")
profiler2 = cProfile.Profile()
profiler2.enable()
result2 = filter_valid_items_v2(allowed_products, products_to_check)
profiler2.disable()

print(f"Filtered to {len(result2)} valid items")
stats2 = pstats.Stats(profiler2)
stats2.sort_stats('cumulative')
stats2.print_stats(5)

print("\n" + "=" * 60)
print("Set lookup (O(1)) is much faster than list lookup (O(n))!")
print("=" * 60)