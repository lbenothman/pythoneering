# Walrus Operator (:=)

Assign and use variables in one expression. Python 3.8+

## The Problem

```python
# Call the function twice
results = [process(n) for n in numbers if process(n) > 5]

# Unnecessary temporary variable
length = len(some_list)
if length > 10:
    print(f"List has {length} items")
```

## The Solution

```python
# Call process() only once per item
results = [result for n in numbers if (result := process(n)) > 5]

# Assign and use in one line
if (length := len(some_list)) > 10:
    print(f"List has {length} items")
```

## Benefits

**Avoid duplicate calls:**
```python
# Before
data = get_data()
if data:
    process(data)

# After
if (data := get_data()):
    process(data)
```

**Efficient list comprehensions:**
```python
[result for x in items if (result := expensive_op(x)) > threshold]
```

**Cleaner regex:**
```python
if (match := re.search(pattern, text)):
    print(match.group(1))
```

## Usage

```bash
python main.py
```

## When to Use

- Avoiding duplicate expensive function calls
- List comprehensions with filtered computed values
- Regex matching with immediate use
- Conditions that need the computed value

## When NOT to Use

Don't sacrifice readability for cleverness. Use it when it genuinely improves code clarity and efficiency.