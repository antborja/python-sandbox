import numpy as np

## PROBLEM SET 2
# 1. Array with 2 dimensions
arr = np.array([1,2,3,4], ndmin=2)  # ndmin = minimum number of dimensions
print("1. ", arr, '\n')

# 2. Check dimension of array
print("2. ", arr.ndim, '\n')

## PROBLEM SET 3
# 3. Indexing
arr = np.array([[[1,2], [3,4]], [[5,6], [7,8]]])
print("3. \nArray:", arr, "arr[1,1,0]:", arr[1,1,0])

## PROBLEM SET 4