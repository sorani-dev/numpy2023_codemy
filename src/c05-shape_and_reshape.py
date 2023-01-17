import numpy as np

# Create a 1-D Numpy array and get its Shape
np1dim = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(np1dim)
"""
[ 1  2  3  4  5  6  7  8  9 10 11 12]
"""
# Get the shape
print(np1dim.shape)
"""
(12,)
"""

# Create a 2-D Numpy array and get its Shape (number of row, number of columns)
np2dim = np.array([[1, 2, 3, 4, 5, 6],[7, 8, 9, 10, 11, 12]])
print(np2dim)
"""
[[ 1  2  3  4  5  6]
 [ 7  8  9 10 11 12]]
"""

print(np2dim.shape)
"""
(2, 6)
"""

# Reshape a 2-D array
np3 = np1dim.reshape((3, 4)) # 3 rows * 4 columns =  of the initizl array12 elements
print(np3)
"""
(3, 4)
"""

print(np3.shape)
"""
(3, 4)
"""

# Reshape a 3-D array
np4 = np1dim.reshape((2, 3, 2))
print("2*3*2", np4, np4.shape)
"""
2*3*2 [[[ 1  2]
  [ 3  4]
  [ 5  6]]

 [[ 7  8]
  [ 9 10]
  [11 12]]] (2, 3, 2)
"""

# Flatten to a 1-D array
np5 = np4.reshape(-1)
print(np5)
print(np5.shape)
"""
[ 1  2  3  4  5  6  7  8  9 10 11 12]
(12,)
"""