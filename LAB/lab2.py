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
'Using import method'

import math
a=336
b=54
print(f"The H.C.F or g.c.d  of {a} and {b} is {math.gcd(a, b)}")


# or
'Using individual function to calc'

def GCD(a,b):
    x=1
    small=a if a<b else b
    for i in range(1,small+1):
        if(a%i==0 and b%i==0):
            x=i
    return x

    

print(GCD(336,54))


def gcd(a,b):
    small = a if a<b else b
    output = [i for i in range(1,small+1) if a%i == 0 and b%i == 0]
    print(output)
    return output[-1]
print(f"The op is {gcd(336,54)}")
