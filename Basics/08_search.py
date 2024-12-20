import numpy as np

# search in array where()

# arr = np.array([1,2,3,4,5,4,4])
# x = np.where(arr==4)
# print(x) # return a array of index

# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# x = np.where(arr%2 == 0)
# print(x)

#  search sorted 
# searchsorted()

# arr = np.array([6, 7, 8, 9])

# x = np.searchsorted(arr, 7)

# print(x)

# arr = np.array([6, 7, 8, 9])

# # x = np.searchsorted(arr, 7,side='right')

# x = np.searchsorted(arr, [2, 4, 6])
# print(x)

#  sorting ++++++++++++++++++++++++++++

# arr = np.array([3,45,0,6,7])
# print(np.sort(arr))

# arr = np.array([True, False, True])

# print(np.sort(arr))

# arr = np.array(['banana', 'cherry', 'apple'])

# print(np.sort(arr))

# arr = np.array([[3, 2, 4], [5, 0, 1]])

# print(np.sort(arr))

# ++++++++++++++Filter +++++++++++

# arr = np.array([41,42,43,44])
# x = [True,False,True,False]
# newArr = arr[x]
# print(newArr)


# arr = np.array([41,42,43,44])

# filter_arr =[]
# for element in arr:
#     if element >42:
#         filter_arr.append(True)
#     else:
#         filter_arr.append(False)

# newArr = arr[filter_arr]
# print(filter_arr)
# print(newArr)


arr = np.array([41, 42, 43, 44])

filter_arr = arr > 42

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)