'''Eutai line ma lekhepani eutai ho or comment garera lekheni tei ho re'''
a=[1,2,3,4]
print(a)
a=[4,5,6,
7,8,8,8,]
print(a)

x=4300
y=100
z=1000
#n
if x\
    <y\
        <z:
    print("True")
else:
    print("False")


x=6
if x<5:
    print("<5")
elif x<7:
    print("<7")
else:
    print(">7")


'''>>Ternary Operation'''
xx=30
b='xx is <33' if xx<33 else 'xx>=33'
print(b)

# from math import sqrt
import math
# o=sqrt(25)
print(math.sqrt(100))






#try statements
#try..catch....finally


# a=10
# b=1

# try:
#     a/b
# except ZeroDivisionError:
#     print("zero div error")
# finally:
#     print("this is printed anyways let it be any scenario")




a=0
b=2

while a<3:
   
    try:
        a/b
    except ZeroDivisionError:
        print("Its zero div error")
    finally:
        # print("value of a is {} and value of b is {}".format(a,b))
        print(f"value of a is {a} and value of b is {b}")
    a=a+1
    b=b-1

print("----------------------------------------------------------------------------------------------------------")



"""For Loops"""
for x in range(10):
    print(x)

for x in 'Hello Python ':
    print(x)

for x in (1,2,3,4,5):
    print(x)


for x in ['H','e','l','l','o']:
    print(x)



for x,xx in [(1,11),(3,44)]:
    print(x,xx)


'''Enumerate returns the index and value of the data in a tupple'''


name="Jenish"
for i,j in enumerate(name):
    print(i,j)

print("----------------------------------------------------------------------------------------------------------")
'''Class'''

class rectangle:
    def __init__(self,l,w):
        self._length=l
        self._width=w

r1=rectangle(100, 200)

print(r1._length)
print(r1._width)



class rectangle:
    def __init__(self,l,w):
        self._length=l
        self._width=w

    def area(self):
        return(self._width*self._length)


    def perimeter(self):
        return((2*self._length)+2*self._width)


    def __str__(self):
        return(f"Width of the object is {self._width} and length of the object is {self._length}")


    def __repr__(self):
        # print(f"rectangle{self._length},{self._width}")
        # return(f"rectangle{self._length},{self._width}")
        return("rectangle({0},{1})".format(self._length,self._width))

    def __eq__(self, other):
        if isinstance(other, rectangle):
            return(self._length==other._length and self._width==other._width)
        else:
            return False
       

r1=rectangle(100, 200)
r2=rectangle(100, 200)

print(str(r1))
print("----------------------------------------------------------------------------------------------------------")

print(repr(r1))
print("----------------------------------------------------------------------------------------------------------")

print(r1.area())

print("----------------------------------------------------------------------------------------------------------")
print(r1.perimeter())

print("----------------------------------------------------------------------------------------------------------")
print(r1 is r2)
print("----------------------------------------------------------------------------------------------------------")

print(r1==r2)
print("----------------------------------------------------------------------------------------------------------")

# print(eq(r1=100))

'''The syntax of isinstance() is:

isinstance(object, classinfo)

isinstance() Parameters

isinstance() takes two parameters:

    object - object to be checked
'''