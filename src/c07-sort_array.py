import numpy as np

# Sort an array: np.sort()
# Returns a copy of the array

np1 = np.array([6, 7, 4, 9, 0, 2, -1, 1])
print(np1)
"""
[ 6  7  4  9  0  2 -1  1]
"""

# Sort numbers from low to high (ascending order)
print(np.sort(np1))
"""
[-1  0  1  2  4  6  7  9]
"""

# Sort Alphabetical values
np2 = np.array(["John", "Tina", "Sophia", "Fatima", "Sigfried", "Alexandre", "Aron", "Zed"])
print(np2)
"""
['John' 'Tina' 'Sophia' 'Fatima' 'Sigfried' 'Alexandre' 'Aron' 'Zed']
"""

print(np.sort(np2))
"""
['Alexandre' 'Aron' 'Fatima' 'John' 'Sigfried' 'Sophia' 'Tina' 'Zed']
"""

# Sort Booleans T/F
np3 = np.array([True, False, False, True])
print(np3)
"""
[ True False False  True]
"""

print(np.sort(np3))
"""
[False False  True  True]
"""

# Sort a 2-D array
np4 = np.array([[6,7,1,9], [8,3, 5,8]])
print(np4)
"""
[[6 7 1 9]
 [8 3 5 8]]
"""
print(np.sort(np4))
"""
[[1 6 7 9]
 [3 5 8 8]]
"""