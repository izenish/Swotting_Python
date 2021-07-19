import numpy as np
from time import perf_counter
import random
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
 #dot product the cumbersome way;
dot=0
def cumbersome_dotproduct(l1,l2):
     for i in range(len(l1)):
          dot+=l1[i]*l2[i]
     return (dot)

def numpy_dotproduct(a,b):
     return np.dot(a,b)
'the same using numpy'
a1=np.array([1,2,3])
a2=np.array([3,4,5])
dot=np.dot(a1,a2)
print(dot)
print("-------------------------")

a=np.random.randn(1000)
b=np.random.randn(1000)
A=list(a)
B=list(b)
# print(b)


'Speed TEST'
def cumbersome_dotproduct(l1,l2):
     dot=0
     for i in range(len(l1)):
          dot+=l1[i]*l2[i]
     return (dot)

def numpy_dotproduct(a,b):
     return np.dot(a,b)

   


start=perf_counter()
for x in range(1000):
     cumbersome_dotproduct(A,B)
end=perf_counter()
cost=end-start
r1=cost
print(f"Using cumbersome method it took {cost} seconds")

start=perf_counter()
for x in range(1000):
     numpy_dotproduct(A,B)
end=perf_counter()
cost=end-start
print(f"Using numpy method it took {cost} seconds")

print(f"Ratio is {r1/cost}")

print("-------------------------")
'Multi dimensional array'
a=np.array([[1,2],[3,3]])
print(a)
print(f"Number of rows,number of columns {a.shape}")

'We can also Transform the matrix using mumpy'
print(f'This is the transformed matrix A {a.T}')

'Calculating Inverse'
print(f'Using Lin calculate inverse {np.linalg.inv(a)}')

'Fancy indexing'
a=np.array([10,2,124,23,1,6])
b=[1,3,5]
print(a[b]) #so this only displayed the corresponding idexed values 

"Only even numbers from the array"
even=np.argwhere(a%2==0).flatten()
print(a[even])

'Reshaping arrays'
a=np.array(range(1,7))
#or
a=np.arange(1,7)
print(a)
print(a.shape)
'Transforming it into:'
b=a.reshape((3,2))
print(b)
print(b.shape)
