"""
tracemalloc - Memory Profiling
"""

import tracemalloc


# Example 1: Basic Memory Tracking
print("Example 1: Basic Memory Tracking")
print("=" * 60)

# Start tracking memory
tracemalloc.start()

# Create some data
print("\nCreating data structures...")
data = []
for i in range(100000):
    data.append({"id": i, "value": i * 2, "name": f"item_{i}"})

# Get memory snapshot
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')

print("\nTop 5 memory allocations:")
for stat in top_stats[:5]:
    print(f"{stat}: {stat.size / 1024:.1f} KB")

# Get current and peak memory usage
current, peak = tracemalloc.get_traced_memory()
print(f"\nCurrent memory usage: {current / 1024 / 1024:.2f} MB")
print(f"Peak memory usage: {peak / 1024 / 1024:.2f} MB")

tracemalloc.stop()


# Example 2: Comparing Memory Usage - List vs Generator
print("\n\nExample 2: Comparing Memory Usage - List vs Generator")
print("=" * 60)


def process_with_list(n):
    """Load all data into memory at once."""
    return [i * i for i in range(n)]


def process_with_generator(n):
    """Generate data on-demand (memory efficient)."""
    return (i * i for i in range(n))


# Test with list
print("\nVersion 1: Using list (loads everything into memory):")
tracemalloc.start()

result_list = process_with_list(1000000)
snapshot1 = tracemalloc.take_snapshot()
current1, peak1 = tracemalloc.get_traced_memory()

print(f"Memory used: {current1 / 1024 / 1024:.2f} MB")
print(f"Peak memory: {peak1 / 1024 / 1024:.2f} MB")

tracemalloc.stop()

# Test with generator
print("\nVersion 2: Using generator (lazy evaluation):")
tracemalloc.start()

result_gen = process_with_generator(1000000)
snapshot2 = tracemalloc.take_snapshot()
current2, peak2 = tracemalloc.get_traced_memory()

print(f"Memory used: {current2 / 1024 / 1024:.2f} MB")
print(f"Peak memory: {peak2 / 1024 / 1024:.2f} MB")

tracemalloc.stop()

# Show the difference
memory_saved = current1 - current2
print(f"\n{'=' * 60}")
print(f"Memory saved: {memory_saved / 1024 / 1024:.2f} MB")
print(f"Generator uses {(current2 / current1) * 100:.1f}% of list memory!")
print(f"{'=' * 60}")