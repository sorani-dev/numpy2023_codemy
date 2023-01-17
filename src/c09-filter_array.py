import numpy as np

# Filtering Numpy Arrays with Boolean Index Lists
np1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# List of values: True: value to keep, False: value to exclude
x = [True, True, False, False, False, False, False, False, False, False]

print(np1)

print("-" * 30)

"""
[ 1  2  3  4  5  6  7  8  9 10]
"""
# Filter np1 array with x
print(np1[x])
"""
[1 2]
"""

print("-" * 30)

# Filtered list
filtered = []
for n in np1:
    if n % 2 == 0:
        filtered.append(True)
    else:
        filtered.append(False)

print(filtered)
"""
[False, True, False, True, False, True, False, True, False, True]
"""
filtered = [x % 2 == 0 for x in np1]
print(filtered)
"""
[False, True, False, True, False, True, False, True, False, True]
"""
new = np1[filtered]
print(new)
"""
[ 2  4  6  8 10]
"""

print("-" * 30)

# Anything greater than 5
filtered = [x > 5 for x in np1]
print(np1[filtered])
"""
[ 6  7  8  9 10]
"""

print("-" * 30)

# Shortcut!
# Even numbers
filtered = np1 % 2 == 0
print(filtered)
print(np1[filtered])
"""
[False  True False  True False  True False  True False  True]
[ 2  4  6  8 10]
"""

print("-" * 30)

# Odd numbers
filtered = np1 % 2 == 1
print(filtered)
print(np1[filtered])
"""
[ True False  True False  True False  True False  True False]
[1 3 5 7 9]
"""

print("-" * 30)

# Numbers greater than five
filtered = np1 > 5
print(filtered)
print(np1[filtered])
"""
[False False False False False  True  True  True  True  True]
[ 6  7  8  9 10]
"""