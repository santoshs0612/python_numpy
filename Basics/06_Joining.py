import numpy as np 

# joining a numpy array 

# arr1 = np.array([1,2,3])
# arr2 = np.array([4,5,6])
# arr = np.concatenate((arr1,arr2))
# print(arr)

# arr1 = np.array([[1,2],[3,4]])
# arr2 = np.array([[5, 6], [7, 8]])
# arr = np.concatenate((arr1,arr2), axis=1) # along row so axis =1 

# print(arr)

# Joining array using stack Function along colum 
# # stacking along new axis along column 
# arr1 = np.array([1,2,3])
# arr2 = np.array([4,5,6])
# arr = np.stack((arr1,arr2),axis=1)
# print(arr)

# # stacking along rows hstack()
# arr1 = np.array([1,2,3])
# arr2 = np.array([4,5,6])
# arr = np.hstack((arr1,arr2))
# print(arr)

# # stacking along colum vstack()
# arr1 = np.array([1,2,3])
# arr2 = np.array([4,5,6])
# arr = np.vstack((arr1,arr2))
# print(arr)

# stacking along depth dstack()
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
arr = np.dstack((arr1,arr2))
print(arr)