import numpy as np
import matplotlib.pyplot as plt

# Declaring arrays
a = np.array([1,2,3], dtype='int32')
print(a)

b = np.array([[9.0, 8.0, 7.0],[6.0,5.0, 4.0]])
print(b)

# Getting dimensions of arrays
print("Dimensions of arrays")
print(a.ndim)
print(b.ndim)

# Getting shape of arrays
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
print(c[0, 1:6:2])  # Subarray is inclusive beginning and exclusing ending

# Modifying data
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

# Initializing arrays with 1 (Special fxn)
a = np.ones(5, dtype='int32')
b = np.ones((2,2), dtype='int32')
print(a)
print(b)

# Initializing arrays with any other number
a = np.full((3,3), 99, dtype='float32')
print(a)

# Initializing an array LIKE another
a = np.full_like(b, 100)
print(a)


