import numpy as np

# Create an array of 10 zeros
print(np.zeros(10))

# Create an array of 10 ones
print(np.ones(10))

# Create an array of 10 fives
print(np.ones(10) * 5)

# Create an array of integers from 10 to 50
print(np.arange(10, 51))

# Create an array of all the even integers from 10 to 50
arr = np.arange(10, 51)
print(arr[arr % 2 == 0])

# Create a 3x3 matrix with the values ranging from 0 to 8
print(np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]]))

# Create a 3x3 identity matrix
print(np.eye(3))

# Use NumPy to generate a random number between 0 and 1
print(np.random.rand(1))

# Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution
print(np.random.randn(5, 5))

# Create the following matrix:
print((np.arange(1, 101) / 100).reshape(10, 10))

# Create an array of 20 linearly spaced points between 0 and 1:
print(np.linspace(0, 1, 20))

# NUMPY INDEXING AND SELECTION
mat = np.arange(1, 26).reshape(5, 5)
'''
print(mat)

[[ 1  2  3  4  5]
 [ 6  7  8  9 10]
 [11 12 13 14 15]
 [16 17 18 19 20]
 [21 22 23 24 25]]
'''

print(mat[2:, 1:])
'''
[[12 13 14 15]
 [17 18 19 20]
 [22 23 24 25]]
'''

print(mat[3, -1])  # 20

print(mat[-1])  # [21 22 23 24 25]

print(mat[3:])
'''
[[16 17 18 19 20]
 [21 22 23 24 25]]
'''

# Get the sum of all the values in mat
print(np.sum(mat))  # 325

# Get the standard deviation of the values in mat
print(np.std(mat))  # 7.211102550927978

# Get the sum of all the columns in mat
print(mat.sum(axis=0))  # [55 60 65 70 75]
