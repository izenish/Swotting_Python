import numpy as np
from numpy.core.fromnumeric import shape
print(np.__version__)

print("-------------------------")
a=np.array([1,2,3])
print(a)
print(a.shape)  #method to know dim
print(a.dtype)  #array data type
print(a.ndim)   #number of dimensions
print(a.size)  #number of elements in array
print(a.itemsize)


print("-------------------------")

print(a[0])  #access it as normal array
a[0]=10
print(a[0])

b=a*np.array([2,0,2])
print(b)

print("-------------------------")
'Diff bet numpy array and python array'
l=[1,2,3]  #normal array
a=np.array([1,2,3])  #numpy array
print(l)
print(a)