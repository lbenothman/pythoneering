import os
from contextlib import suppress

# Instead of:
try:
    os.remove('file.txt')
except FileNotFoundError:
    pass

# Use:
with suppress(FileNotFoundError):
    os.remove('file.txt')


# More examples:

# Example 1: Suppress multiple exceptions
with suppress(FileNotFoundError, PermissionError):
    os.remove('protected_file.txt')

# Example 2: Clean up temporary files
temp_files = ['temp1.txt', 'temp2.txt', 'temp3.txt']
for file in temp_files:
    with suppress(FileNotFoundError):
        os.remove(file)

# Example 3: Dictionary operations
data = {'key1': 'value1'}
with suppress(KeyError):
    del data['nonexistent_key']

# Example 4: List operations
my_list = [1, 2, 3]
with suppress(ValueError):
    my_list.remove(999)  # Element doesn't exist

print("All operations completed successfully!")