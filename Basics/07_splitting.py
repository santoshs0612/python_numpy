import numpy as np

# splitting array 

# arr = np.array([1,2,3,4,5,6])
# # newArr = np.array_split(arr,3)

# newArr = np.array_split(arr,4);
# print(newArr)
# print(newArr[0])
# print(newArr[1])

arr = np.array([[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]])
newArr = np.array_split(arr,3)
print(newArr)