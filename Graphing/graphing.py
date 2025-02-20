import numpy as np
import matplotlib.pyplot as plt

# Declaring arrays
a = np.array([1,2,3], dtype='int32')
print(a)

b = np.array([[9.0, 8.0, 7.0],[6.0,5.0, 4.0]])
print(b)

# Getting dimensions of arrays (2D, 3D, etc)
print("Dimensions of arrays")
print(a.ndim)
print(b.ndim)

# Getting shape of arrays (row, col)
print("Getting shape of arrays")
print(a.shape)
print(b.shape)

# -----------------------------------------------
print("\n-------------Accessing arrays-------------\n")

c = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])
print(c)

# Get a specific element [r, c]
print(c[1,5])
print(c[1,-2])

# Get specific row
print(c[0, :])

# Get a specific column
print(c[:,2])

# Other functions
print(c[0, 1:6:2])  # Subarray is inclusive beginning and exclusing ending. Third param is for increments

# Modifying data (NOTE: REFER TO EXERCISES FOR ARRAY IN ARRAY)
c[0,0] = 100
print(c)

c[:,:] = 100
print(c)

# -----------------------------------------------
print("\n-------------Initializing arrays-------------\n")

# Initializing arrays with 0. (Special fnx)
a = np.zeros(5)
b = np.zeros((2,2))
print(a)
print(b)

# Creating and initializing arrays with 1 (Special fxn)
a = np.ones(5, dtype='int32')
b = np.ones((2,2), dtype='int32')
print(a)
print(b)

# Initializing arrays with any other number
a = np.full((3,3), 99, dtype='float32')
print(a)

# Initializing an array LIKE another. Assumes shape
a = np.full_like(b, 100)
print(a)

# Initializing with random decimals (integers of the shape)
a = np.random.rand(3,2)
print(a)

# Random integer (0-7)
a = np.random.randint(7, size=(3,3))
print(a)

# Random int (4-7)
a = np.random.randint(4,7, size=(3,3))
print(a)

# Identity matrix
a = np.identity(3)
print(a)

# Repeating arrays
arr = np.array([1,2,3])
r1 = np.repeat(arr, 3)
print(r1)

arr = np.array([[1,2,3]])
print(arr)
r1 = np.repeat(arr, 3, axis=0)
print(r1)

# Exercise 1
a = np.ones((5,5), dtype='int32')
b = np.zeros((3,3), dtype='int32')
b[1,1] = 9
a[1:4,1:4] = b
print (a)

# Pointers
a = np.array([1,2,3])
b = a
b[0] = 100
print(b)
print(a)

a = np.array([1,2,3])
b = a.copy()
print(b)
print(a)

# -----------------------------------------------
print("\n-------------MATHEMATICS-------------\n")