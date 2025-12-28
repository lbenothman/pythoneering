# functools.partial

Pre-fill function arguments to create specialized versions.

## The Problem

```python
# Repetitive function calls with same arguments
log("ERROR", "Database connection failed")
log("ERROR", "Invalid credentials")
log("ERROR", "Timeout occurred")

# Verbose lambda in map/filter
list(map(lambda x: int(x, base=16), hex_numbers))
```

## The Solution

```python
from functools import partial

# Create specialized function
log_error = partial(log, "ERROR")
log_error("Database connection failed")
log_error("Invalid credentials")

# Cleaner map operations
parse_hex = partial(int, base=16)
list(map(parse_hex, hex_numbers))
```

## Benefits

**Reduce repetition:**
```python
# Before
requests.get(url1, timeout=10, headers=auth_headers)
requests.get(url2, timeout=10, headers=auth_headers)

# After
api_get = partial(requests.get, timeout=10, headers=auth_headers)
api_get(url1)
api_get(url2)
```

**Better than lambda:**
```python
# Lambda loses identity
f = lambda x: int(x, base=16)
print(f.__name__)  # '<lambda>'

# Partial preserves function info
f = partial(int, base=16)
print(f.func.__name__)  # 'int'
```

**Function factories:**
```python
def multiply(a, b):
    return a * b

double = partial(multiply, 2)
triple = partial(multiply, 3)

double(5)  # 10
triple(5)  # 15
```

## Usage

```bash
python main.py
```

## When to Use

- Repeatedly calling a function with same arguments
- Creating callbacks with pre-filled data
- Cleaner map/filter operations
- Building function factories
- When you need picklable functions (unlike lambdas)

## When NOT to Use

Don't use when a simple lambda is clearer for one-off use, or when the function is only called once.