# cProfile - Performance Profiling

Find performance bottlenecks in your code. Python standard library.

## The Problem

```python
# Your code is slow but you don't know why
def slow_function():
    # Which part is the bottleneck?
    result1 = expensive_operation1()
    result2 = expensive_operation2()
    result3 = expensive_operation3()
    return combine(result1, result2, result3)

# Guessing what's slow leads to wasted optimization effort
```

## The Solution

```python
import cProfile
import pstats

# Profile your code
profiler = cProfile.Profile()
profiler.enable()

slow_function()

profiler.disable()

# Analyze results
stats = pstats.Stats(profiler)
stats.sort_stats('cumulative')
stats.print_stats(10)  # Show top 10 slowest functions
```

## Benefits

**Find real bottlenecks:**
```python
# See exactly which functions take the most time
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#   1000    0.050    0.000    0.150    0.000 module.py:42(slow_function)
```

**Compare implementations:**
```python
# Profile version A
profiler_a = cProfile.Profile()
profiler_a.enable()
implementation_a()
profiler_a.disable()

# Profile version B
profiler_b = cProfile.Profile()
profiler_b.enable()
implementation_b()
profiler_b.disable()

# Compare which is faster
```

**Measure impact of optimizations:**
```python
# Profile before optimization
# Optimize
# Profile after optimization
# Verify actual improvement with data
```

## Understanding the Output

```
ncalls    - Number of times function was called
tottime   - Total time spent in function (excluding subfunctions)
percall   - tottime / ncalls
cumtime   - Total time including subfunctions
percall   - cumtime / ncalls
```

## Usage

```bash
python main.py
```

Or profile any script:
```bash
python -m cProfile -s cumulative your_script.py
```

## When to Use

- Code is slow and you need to find bottlenecks
- Comparing performance of different implementations
- Verifying optimization improvements
- Understanding where your program spends time
- Before scaling or refactoring

## When NOT to Use

Don't profile in production (overhead cost), or for micro-benchmarks (use `timeit` instead). Profile during development to guide optimization decisions.