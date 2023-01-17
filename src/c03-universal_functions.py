import numpy as np

# Numpy Universal Functions or UFuncs
# @see https://numpy.org/doc/stable/reference/ufuncs.html

# Declare array
np1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(np1)
"""
[0 1 2 3 4 5 6 7 8 9]
"""

# Find square root of each element √n
print(np.sqrt(np1))
"""
[0.         1.         1.41421356 1.73205081 2.         2.23606798
 2.44948974 2.64575131 2.82842712 3.        ]
 """

np_negint_array = np.array([-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# Absolute value |x|
print(np.abs(np_negint_array))
"""
[3 2 1 0 1 2 3 4 5 6 7 8 9]
"""

# Exponential of array (e^n)
print(np.exp(np_negint_array))
"""
[4.97870684e-02 1.35335283e-01 3.67879441e-01 1.00000000e+00
 2.71828183e+00 7.38905610e+00 2.00855369e+01 5.45981500e+01
 1.48413159e+02 4.03428793e+02 1.09663316e+03 2.98095799e+03
 8.10308393e+03]
 """
# Min/Max of array
print(np.min(np_negint_array), np.max(np_negint_array))
"""
-3 9
"""

# Find the Sign of the numbers in the array (-1 if negative, 0 if zeo, 10 if positive
print(np.sign(np_negint_array))
"""
[-1 -1 -1  0  1  1  1  1  1  1  1  1  1]
"""

# Trigonometry function: sinus(x)n cosinus(x), log(x)
print(np.sin(np1))
"""
[ 0.          0.84147098  0.90929743  0.14112001 -0.7568025  -0.95892427
 -0.2794155   0.6569866   0.98935825  0.41211849]
"""

print(np.log(np1))
"""
[      -inf 0.         0.69314718 1.09861229 1.38629436 1.60943791
 1.79175947 1.94591015 2.07944154 2.19722458]
"""
