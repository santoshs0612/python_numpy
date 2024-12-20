import numpy as np

# Python have data types of string, integer,float, boolean, complex

# numpy has darta types of 
# i integer 
# b boolean 
# u unsigned integer
# f float
# c complex float
# m timedelta
# M datetime 
# O object 
# S string
# U unicode string 
# V fixed chunk of memory 



# //data types 

# arr =np.array([1,2,3,4,5])
# print(arr.dtype)

# arr = np.array(["apple" , "Banana", "Chery"])

# print(arr.dtype)

# defining the data types 

# arr = np.array([1,2,3,4],dtype='S')
# print(arr)
# print(arr.dtype)

# we can also define size of datatypes 

arr = np.array([1,2,3,4],dtype='i4')
print(arr)
print(arr.dtype)

# vlaue Error when we cant convert the type like string to integer 
# arr = np.array(['a','2','3'],dtype='i') a has an errpr/

# converting datatype after making a copy 

# astype()
arr = np.array([1.1,2.4,6.7])
newArr = arr.astype('i')
print(arr)
print(newArr)

