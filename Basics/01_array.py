import numpy as np

arr = np.array([1,2,3,4])

# print(arr)
# print(np.__version__)
# print(np.__all__)

# print(type(arr))

# numpy array with tuple
arr = np.array((1,2,3,4))
# print(arr)
# // zero dimension 
arr1 = np.array(45)
print(arr1);

# 2 dimension 

arr2 = np.array([[1,2,3],[4,5,6]])
# print(arr2)

print(arr.ndim);
print(arr1.ndim);
print(arr2.ndim);

arr5 = np.array([1,2,3,4,5],ndmin=5)
print(arr5)

print(arr[1])
print('print the value of 2nd element', arr2[0,2]);


# // slicing in the numpy array 


print(arr2[:1])

arr0 = np.array([1, 2, 3, 4, 5, 6, 7])
# slice it from back 

# print(arr0[-3:-1])

# 



