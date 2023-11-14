import numpy as np

# Create a 2x3 matrix of ones
# m = np.ones((2, 3))

# Create a 3x2 matrix of zeros
# a = np.arange(3)

# Reshape a to a 3x1 matrix
# reshapedA = a.reshape(3, 1)

# Add the two matrices
# print(a + reshapedA)


# -----------------------


# Create a 10x3 matrix of random numbers between 0 and 1
# x = np.random.random((10, 3))

# Find the mean of each column, across all rows
# x_mean = x.mean(axis=0)

# Subtract the mean from each column
# x_centered = x - x_mean



# a = np.array([[1, 2, 3], [4, 5, 6]])
# b = np.array([[7, 8, 9], [10, 11, 12]])
# print(a + b) # Output: array([[ 8, 10, 12], [14, 16, 18]])
# print(a - b) # Output: array([[-6, -6, -6], [-6, -6, -6]])
# a and b can not be multiplied because they have different shapes


# a = np.array([[2, 3], [4, 5]])
# b = np.array([[6, 7], [8, 9]])
# print(a * b)  # Output: array([[12, 21], [32, 45]])
# print(np.dot(a, b))  # Output: array([[36, 41], [64, 73]])
# Notice that the a * b and np.dot(a, b) are different