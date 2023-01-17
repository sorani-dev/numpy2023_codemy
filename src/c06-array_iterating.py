import numpy as np

# For 1-D array
np1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Loop through array: standard Python iteration
for x in np1:
    print(x)
"""
1
2
3
4
5
6
7
8
9
10
"""

# 2-D array
np2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

# Print array row by row
for x in np2:
    # Print rows
    print(x)
"""
[1 2 3 4 5]
[ 6  7  8  9 10]
"""

# Print a signle element from an array
for x in np2:
    for y in x:
        print(y)
"""
1
2
3
4
5
6
7
8
9
10
"""

print()

# 3-D array
np3 = np.array(
    [
        [[1, 2, 3], [4, 5, 6]],
        [[7, 8, 9], [10, 11, 12]],
        [[13, 14, 15], [16, 17, 18]],
    ]
)
# Loop through the 1st dimension: display a 2-D array
for x in np3:
    print(x)
"""
[[1 2 3]
 [4 5 6]]
[[ 7  8  9]
 [10 11 12]]
[[13 14 15]
 [16 17 18]]
"""

# Print all invidual elements of a 3-D array
for x in np3:
    for y in x:
        for z in y:
            print(z)

"""
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
"""

# Use nditer to loop through array
for x in np.nditer(np3):
    print(x)

"""
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
"""