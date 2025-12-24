# tracemalloc - Memory Profiling

Track memory usage and find memory leaks. Python standard library.

## The Problem

```python
# Your app uses too much memory but you don't know where
def process_data(items):
    # Which operations consume the most memory?
    result1 = load_data()
    result2 = transform_data(result1)
    result3 = aggregate_data(result2)
    return result3

# Guessing what uses memory leads to wrong optimizations
```

## The Solution

```python
import tracemalloc

# Start tracking memory
tracemalloc.start()

process_data(items)

# Get memory usage
current, peak = tracemalloc.get_traced_memory()
print(f"Current: {current / 1024 / 1024:.2f} MB")
print(f"Peak: {peak / 1024 / 1024:.2f} MB")

tracemalloc.stop()
```

## Benefits

**Track memory allocations:**
```python
# See which lines allocate the most memory
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')

for stat in top_stats[:10]:
    print(stat)
```

**Compare memory usage:**
```python
# List loads everything into memory
data_list = [i * i for i in range(1000000)]  # 38 MB

# Generator creates items on-demand
data_gen = (i * i for i in range(1000000))   # ~0 MB

# Generator saves 38 MB of memory!
```

**Find memory leaks:**
```python
# Take snapshots before and after
snapshot1 = tracemalloc.take_snapshot()
# ... run your code ...
snapshot2 = tracemalloc.take_snapshot()

# See what changed
diff = snapshot2.compare_to(snapshot1, 'lineno')
for stat in diff[:10]:
    print(stat)
```

## Understanding the Output

```
current - Current memory allocated by traced objects
peak    - Maximum memory used during execution
size    - Memory allocated in bytes/KB/MB
count   - Number of allocations
```

## Usage

```bash
python main.py
```

## When to Use

- App uses too much memory
- Comparing memory efficiency of implementations
- Finding memory leaks
- Optimizing memory-intensive operations
- Understanding memory allocation patterns

## When NOT to Use

Don't use in production (has overhead). Use during development to identify memory issues and optimize before deployment.