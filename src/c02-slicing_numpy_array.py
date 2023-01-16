import numpy as np

# Slicing Numpy arrays
np1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# Return 2, 3, 4, 5 ([start:end excluded])
print(np1[1:5])
"""
[2 3 4 5]
"""

# Return from something to the end of the array?
print(np1[3:])
"""
[4 5 6 7 8 9]
"""

# Return negative slices
# 7,8
print(np1[-3:-1])
"""
[7 8]
"""

# Slices using steps
print(np1[1:5])  # 2 through 5
print(np1[1:5:2])  # 2 through 5 in steps of 2
"""
[2 3 4 5]
[2 4]
"""

# Setps on the entire array
print(np1[::2])  # Step of 2
print(np1[::3])  # Step of 3
"""
[1 3 5 7 9]
[1 4 7]
"""

# Slice a 2-d array
np2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# Pull out a single value
print(np2[1,2]) #  2inth item in 1inth item
"""
8
"""

# Slice a 2-d array:
# array[rows, columns]
print(np2[0:1, 1:3])
"""
[[2 3]]
"""

# Slice from both rows 2,3 and 7,8
print(np2[0:2, 1:3])
"""
[[2 3]
 [7 8]]
 """
