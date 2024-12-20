import numpy as np

# arr = np.array([1,2,3])
# for x in arr:
#     print(x)

arr =np.array([[1,2,3,4],[5,6,7,8]])
# for x in arr:
#     print(x)

# for x in arr:
#     for y in x:
#         print(y)


# arr = np.array([[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]])
# print(arr.shape)
# for x in arr:
#     print(x)

# for x in arr:
#     for y in x:
#         for z in y:
#             print(z)


# itersting using nditer()

# iterating each scaler element we need n loops if dimensions increase so use nditer()

# arr = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])

# for x in np.nditer(arr):
#     print(x)


# in iterating eith different data types 

# arr = np.array([1,2,3])

# for x in np.nditer(arr, flags=['buffered'],op_dtypes=['S']):
#     print(x)

# arr = np.array([[1,2,3,4],[5,6,7,8]])
# for x in np.nditer(arr[:,::2]):
#     print(x)

# Enumerated iteration using ndenumerate()

arr = np.array([1,2,3])

for indx,x in np.ndenumerate(arr):
    print(indx,x)