import numpy as np

# Python List
list1 = [1, 2, 3, 4, 5]
print(list1)
print(list1[0])
"""
[1, 2, 3, 4, 5]
1
"""

# Problem: Lists can have data of multiple types
list2 = ["Riku Sorani", 42, list1, True]
print(list2)
"""
['Riku Sorani', 42, [1, 2, 3, 4, 5], True]
"""

# Numpy - Numeric Python
# Data type of numpy array is ndarray which stands for n-dimensional array

np1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(np1)
"""
[0 1 2 3 4 5 6 7 8 9]
"""

# Shape of the array: number of elements in the array.
# Think of the len function in python
print(np1.shape)
"""
(10,)
"""

# np.arange: Create an array of values
np2 = np.arange(10)
print(np2)
"""
[0 1 2 3 4 5 6 7 8 9]
"""

# np.arange with step (start = 0, end = 10, step = 2)
np3 = np.arange(0, 10, 2)
print(np3)
"""
[0 2 4 6 8]
"""

# Create a numpy array of zeros
np4 = np.zeros(10)
print(np4)
"""
[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
"""

# Multi-dimensional zeros array
np5 = np.zeros((2, 10))
print(np5)
"""
[[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]]
"""

# Array filled with a given value
np6 = np.full((10), 6)
print(np6)
"""
[6 6 6 6 6 6 6 6 6 6]
"""

# Multi-dimensional Full
np7 = np.full((2, 10), 6)
print(np7)
"""
[[6 6 6 6 6 6 6 6 6 6]
 [6 6 6 6 6 6 6 6 6 6]]
 """

# Convert Python lists to Numpy
my_list = [1,2,3,4,5]
np8 = np.array(my_list)
print(np8, type(np8))
"""
[1 2 3 4 5] <class 'numpy.ndarray'>
"""

# Get the first item of an np array
print(np8[0])
"""
1
"""
