"""
Python Descriptors for Reusable Attribute Validation
"""


class PositiveNumber:
    """Descriptor that validates positive numbers"""

    def __set_name__(self, owner, name):
        self.name = f"_{name}"

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.name, 0)

    def __set__(self, instance, value):
        if not isinstance(value, (int, float)):
            raise TypeError(f"Expected number, got {type(value).__name__}")
        if value < 0:
            raise ValueError(f"{self.name[1:]} cannot be negative")
        setattr(instance, self.name, value)


class BankAccount:
    """Bank account with validated balance"""

    balance = PositiveNumber()

    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount


if __name__ == "__main__":
    print("=== Valid Operations ===")
    account = BankAccount(100)
    print(f"Initial balance: ${account.balance}")

    account.deposit(50)
    print(f"After deposit: ${account.balance}")

    account.withdraw(30)
    print(f"After withdrawal: ${account.balance}")

    print("\n=== Validation Errors ===")
    try:
        account.balance = -50  # Negative balance
    except ValueError as e:
        print(f"✗ {e}")

    try:
        account.balance = "invalid"  # Wrong type
    except TypeError as e:
        print(f"✗ {e}")

    try:
        account = BankAccount(-100)  # Negative initial balance
    except ValueError as e:
        print(f"✗ {e}")