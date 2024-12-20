import numpy as np 

# arr =np.array([[1,2,3,4],[5,6,7,8]])
# print(arr.shape)

# arr = np.array([1,2,3,4],ndmin=5)
# print(arr)
# print("Shape of array : ", arr.shape)

#  Reshaping of array 

# # Reshape from 1D to 2 D

# arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# newArray = arr.reshape(4,3)
# print(newArray)


# Reshape from 1D to 3 D

# arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# newArray = arr.reshape(2,3,2)
# print(newArray)

#  we can reshape any size aarray as long as elenet are same 

# arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# print(arr.reshape(4,3).base) # this is a view 
# flattening the arrays
arr = np.array([[1,2,3],[4,5,6]])
newArr = arr.reshape(-1)
print(newArr)