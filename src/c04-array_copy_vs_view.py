import numpy as np

# Copy an array versus View an array
# Views are linked by pointer to the array they are copied from (like python lists)
# Create a Copy of an array

# Declare array
np1 = np.array([0, 1, 2, 3, 4, 5])

# Create a View
np_view = np1.view()

print(f"Original NP1 {np1}")
print(f"Original NP2 {np_view}")
"""
Original NP1 [0 1 2 3 4 5]
Original NP2 [0 1 2 3 4 5]
"""

np1[0] = 42

print(f"Changed NP1 {np1}")
print(f"Original NP2 {np_view}")
"""
Changed NP1 [42  1  2  3  4  5]
Original NP2 [42  1  2  3  4  5]
"""

np_view[0] = 1024

print(f"Original NP1 {np1}")
print(f"Changed NP2 {np_view}")
"""
Original NP1 [1024    1    2    3    4    5]
Changed NP2 [1024    1    2    3    4    5]
"""

print(id(np1), id(np_view))
"""
2190453734256 2190453733872
"""

# Create a Copy
np_copy = np1.copy()

print(f"Original NP1 {np1}")
print(f"Original NP2 {np_copy}")
"""
Original NP1 [42  1  2  3  4  5]
Original NP2 [42  1  2  3  4  5]
"""

np1[0] = 0

print(f"Changed NP1 {np1}")
print(f"Original NP2 {np_copy}")
"""
Changed NP1 [0 1 2 3 4 5]
Original NP2 [42  1  2  3  4  5]
"""

np_copy[0] = 1024

print(f"Original NP1 {np1}")
print(f"Changed NP2 {np_copy}")
"""
Original NP1 [0 1 2 3 4 5]
Changed NP2 [1024    1    2    3    4    5]
"""

print(id(np1), id(np_copy))
"""
2587411446640 2585811026736
"""
