# contextlib.suppress - Clean Exception Handling

Stop writing try-except blocks just to ignore exceptions.

## The Problem

You often write code like this:

```python
try:
    os.remove('file.txt')
except FileNotFoundError:
    pass
```

Four lines just to say "delete this file, ignore if it doesn't exist."

## The Solution

Use `contextlib.suppress`:

```python
with suppress(FileNotFoundError):
    os.remove('file.txt')
```

Two lines. Clear intent. Less noise.

## Benefits

**1. Cleaner Code**
- Reduces 4 lines to 2 lines
- No empty `pass` statements
- Intent is immediately clear

**2. More Readable**
- "Suppress this exception" vs "try this, catch that, do nothing"
- The exception type is at the top, not buried in a catch block
- Less visual clutter

**3. Explicit Intent**
- Makes it obvious you're intentionally ignoring the exception
- Different from forgetting to handle an error
- Documents expected failure cases

**4. Multiple Exceptions**
- Can suppress multiple exception types easily:
  ```python
  with suppress(FileNotFoundError, PermissionError):
      os.remove('file.txt')
  ```

**5. No Accidental Catch-All**
- Only catches the exact exceptions you specify
- Won't accidentally hide unexpected errors
- Safer than `except Exception`

## Installation

No dependencies needed - `contextlib` is part of Python's standard library:

## Usage

Run the example:

```bash
python main.py
```

## Common Use Cases

**Cleanup operations:**
```python
with suppress(FileNotFoundError):
    os.remove('temp_file.txt')
```

**Dictionary operations:**
```python
with suppress(KeyError):
    del cache['expired_key']
```

**List operations:**
```python
with suppress(ValueError):
    items.remove(item_to_delete)
```

**Resource cleanup:**
```python
with suppress(AttributeError):
    connection.close()
```

## When NOT to Use

Don't use `suppress` when:
- You need to log the error
- You need to take action on failure
- You need to know if the operation succeeded
- The exception indicates a real problem

Use regular try-except blocks for those cases.

## Anti-Pattern

```python
# DON'T do this
with suppress(Exception):  # Too broad!
    risky_operation()
```

Only suppress specific, expected exceptions.