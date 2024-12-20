import numpy as np

# differnce betweeen copy and view 

# arr = np.array([1,2,3,4,5,6])
# # x = arr.copy()
# x = arr.view()
# arr[0] = 42
# print(arr)
# print(x)


# copy owns a data but the view does not 
arr = np.array([1,2,3,4,5,6])
x = arr.copy()
y = arr.view()

print(x.base) # base returns a none it owns a data
print(y.base) # base return a original 
