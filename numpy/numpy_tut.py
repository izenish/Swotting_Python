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

l.append(4)
# a.append(4) AttributeError: 'numpy.ndarray' object has no attribute 'append'
a=a+np.array([4]) #added 4 to all the elemnts in the array
print(l)
print(a)

l=l*2 #repeats the array twice
a=a*2 #multiplied 2 to each element of the array
print(l)
print(a)
print("-------------------------")

l1=[1,2,3]
l2=[3,4,5]
 #dot product the tedious
dot=0
for i in range(len(l1)):
     dot+=l1[i]*l2[i]
print(dot)

'the same using numpy'
a1=np.array([1,2,3])
a2=np.array([3,4,5])
dot=np.dot(a1,a2)
print(dot)