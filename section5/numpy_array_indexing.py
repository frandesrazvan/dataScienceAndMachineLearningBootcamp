import numpy as np

arr = np.arange(0, 11)

print(arr[8])  # index
print(arr[1:5])  # [1 2 3 4]
print(arr[::2])  # [ 0  2  4  6  8 10]

# arr[0:5] = 100
# print(arr)  # [100 100 100 100 100   5   6   7   8   9  10]

slice_of_arr = arr[0:6]
slice_of_arr[:] = 99
print(slice_of_arr)  # [99 99 99 99 99 99]
print(arr)  # [99 99 99 99 99 99  6  7  8  9 10]

arr_copy = arr.copy()
print(arr)  # [99 99 99 99 99 99  6  7  8  9 10]
print(arr_copy)  # [99 99 99 99 99 99  6  7  8  9 10]
arr_copy[:] = 100
print(arr)  # [99 99 99 99 99 99  6  7  8  9 10]
print(arr_copy)  # [100 100 100 100 100 100 100 100 100 100 100]

# MATRIX
arr_2d = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])
print(arr_2d)

print(arr_2d[0][0])  # 5
print(arr_2d[0])  # [ 5 10 15]

print(arr_2d[2, 1])  # 40

print(arr_2d[:2, 1:])
'''
[[10 15]
 [25 30]]
'''

print(arr_2d[1:2, :])  # [[20 25 30]]
print(arr_2d[1:2])  # [[20 25 30]]

# CONDITIONAL SELECTION

arra = np.arange(1, 11)
bool_arra = arra > 5
print(bool_arra)  # [False False False False False  True  True  True  True  True]
print(arra[bool_arra])  # [ 6  7  8  9 10]

print(arra[arra > 5])  # [ 6  7  8  9 10]
print(arra[arra % 2 == 0])  # [ 2  4  6  8 10]

# EXERCISE

arra_2d = np.arange(50).reshape(5, 10)
print(arra_2d)
'''
[[ 0  1  2  3  4  5  6  7  8  9]
 [10 11 12 13 14 15 16 17 18 19]
 [20 21 22 23 24 25 26 27 28 29]
 [30 31 32 33 34 35 36 37 38 39]
 [40 41 42 43 44 45 46 47 48 49]]
'''

print(arra_2d[1:3, 3:5])
'''
[[13 14]
 [23 24]]
'''
print(arra_2d[arra_2d % 5 == 0])  # [ 0  5 10 15 20 25 30 35 40 45]
