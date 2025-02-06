import numpy as np

my_list = [1, 2, 3]
print(np.array(my_list))

my_mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(np.array(my_mat))

print(np.arange(0, 10, 3))  # [0 3 6 9]

print(np.zeros(3))  # [0. 0. 0.]
print(np.zeros((3, 3)))
'''
[[0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]]
'''

print(np.ones(4))  # [1. 1. 1. 1.]

print(np.linspace(0, 5, 10))
'''
[0.         0.55555556 1.11111111 1.66666667 2.22222222 2.77777778
 3.33333333 3.88888889 4.44444444 5.        ]
'''

print(np.eye(4))
'''
[[1. 0. 0. 0.]
 [0. 1. 0. 0.]
 [0. 0. 1. 0.]
 [0. 0. 0. 1.]]
'''

print(np.random.rand(5))  # [0.14885157 0.29445419 0.04587317 0.69164817 0.68951836]
print(np.random.rand(3, 3))
'''
[[0.99951689 0.19528579 0.47615707]
 [0.59634378 0.81209982 0.52083696]
 [0.8376333  0.5788128  0.35374168]]
'''

print(np.random.randn(2)) # [ 0.47012226 -1.0885899 ]

print(np.random.randint(0, 100, 10))  # [38 81 21  3 15 52  4 19 86 37]

arr = np.arange(25)
print(arr.reshape(5, 5))
'''
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]
 [15 16 17 18 19]
 [20 21 22 23 24]]
'''

ranarr = np.random.randint(0, 50, 10)
print(ranarr)
print(ranarr.max())
print(ranarr.min())
print(ranarr.argmax())  # index location of max value
print(ranarr.argmin())  # index location of min value

print(arr.shape)  # (25,)
arr = arr.reshape(5, 5)
print(arr.shape)  # (5, 5)

print(arr.dtype)  # int64

