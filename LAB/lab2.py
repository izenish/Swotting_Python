#Second Lab On AI
# Python code to demonstrate naive
# method to compute gcd ( Euclidean algo )
  
  
def computeGCD(x, y):
  
   while(y):
       x, y = y, x % y
  
   return x
  
a = 60
b= 48
  
# prints 12
print ("The gcd of 60 and 48 is : ",end="")
print (computeGCD(60,48))



#or

import math
a=64
b=1000
print(f"The H.C.F or g.c.d  of {a} and {b} is {math.gcd(a, b)}")


# or


def GCD(a,b):
    x=1
    small=a if a<b else b
    for i in range(1,small+1):
        if(a%i==0 and b%i==0):
            x=i*x
    return x

    

print(GCD(64,100))


