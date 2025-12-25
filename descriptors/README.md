# Python Descriptors

Reusable attribute validation without repetitive property definitions.

## The Problem

```python
class BankAccount:
    def __init__(self, balance):
        self._balance = None
        self.balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        # Repetitive validation in every class
        if not isinstance(value, (int, float)):
            raise TypeError("Expected number")
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = value

# Same validation code repeated in other classes (Product, Inventory, etc.)
```

## The Solution

```python
class PositiveNumber:
    """Descriptor - write validation once, reuse everywhere"""

    def __set_name__(self, owner, name):
        self.name = f"_{name}"

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.name, 0)

    def __set__(self, instance, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Expected number")
        if value < 0:
            raise ValueError(f"{self.name[1:]} cannot be negative")
        setattr(instance, self.name, value)

class BankAccount:
    balance = PositiveNumber()  # Validation happens automatically

    def __init__(self, balance):
        self.balance = balance  # ✓ Validated
```

## Benefits

- **Reusable** - Write once, use in multiple classes
- **Less code** - No repetitive property definitions
- **Consistent** - Same validation logic everywhere
- **Type safe** - Validation on every assignment

## Installation

```bash
python3 main.py
```

## When to Use

Use when the same validation logic is needed across multiple classes (positive numbers, string length, email format, etc.).

## When NOT to Use

For one-off validation unique to a single class, regular properties are clearer.