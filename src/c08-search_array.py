import numpy as np

# Search
np1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 3])
print(np1)
"""
[ 1  2  3  4  5  6  7  8  9 10  3]
"""

# Search for 3 in np1
x = np.where(np1 == 3)
print(x)
"""
(array([ 2, 10], dtype=int64),)  # 3 is at index number 2 and index number 10
                            # and their datatype is an integer 64 bits
"""
# Get the indexes of the found values
print(x[0])
"""
[ 2 10]
"""

# Get the values of the found indexes
print(np1[x[0]])
"""
[3 3]
"""

# Return the even items
y = np.where(np1 % 2 == 0)
print(y)
print(y[0])
print(np1[y[0]])
"""
(array([1, 3, 5, 7, 9], dtype=int64),)
[1 3 5 7 9]
[ 2  4  6  8 10]
"""

print()

# Return odd items
z = np.where(np1 % 2 == 1)
print(z)
print(z[0])
print(np1[z[0]])
"""
(array([ 0,  2,  4,  6,  8, 10], dtype=int64),)
[ 0  2  4  6  8 10]
[1 3 5 7 9 3]
"""