# print("hello wrold")
# a=10 
# b=10
# hex(id(a))
# hex(id(b))
# print(hex(id(a)) is hex(id(b)))







# def random(**kwargs):
#     print(kwargs)

# random(x=2,e=3,f=55)


# def ran(*args,**kwargs):
#     print(args,kwargs)

# ran(1,2,3,c=3,f=4,grg=44)
import time
import datetime


# def ran(a=1,b=2,*args,c):
#     start=time.perf_counter()
#     print(a,b,args,c,sep="🙄🙄")
#     end=time.perf_counter()
#     print(end-start)

# ran(11,22,'x','y',c=22)


# def zbc(msg,dt=None):
#     dt=dt or datetime.datetime.utcnow()
#     print(f"{msg} sent at {dt}")

# zbc(123444444,2022)
# zbc("This message was")

# print(datetime.datetime.utcnow())



"""Parameter Defaults Beware 2!!, mutable kura haru default ma esari na rakhne kina vane shared huna sakxa or limited hunxa tesaile"""
def add_item(name,quantity,unit,grocessylist=[]):
    grocessylist.append(f"{name} {quantity} {unit}")
    return grocessylist

store1=add_item("apple",1,"kg")
store1=add_item("oranges",1,"kg")

print(store1)

store2=add_item("Sausages",2,"units")
print(store2)


"""both of them started using the same grocerry list because the object defined was shared by both in case of mutable items"""
print("---------------------------------------------------")
"""Mutable kura lai esari immutable banaune"""



def add_item(name,quantity,unit,grocessylist=None):
    if not grocessylist:
        grocessylist=[]
        grocessylist.append(f"{name} {quantity} {unit}")
        return grocessylist

store1=add_item("apple",1,"kg")
store1=add_item("oranges",1,"kg")

print(store1)

store2=add_item("Sausages",2,"units")
print(store2)

print("---------------------------------------------------")


def factorial(n):
    if n<1:
        return 1
    else:
        # print(f"{n}")
        return n*factorial(n-1)

print(factorial(12))

print("---------------------------------------------------")





# def my_func(a, b):
#     'Returns the product of a and b'
#     return a*b

# help(my_func)


# x = 3
# y = 5
# # def my_func(a: str) -> 'a repeated ' + str(max(3, 5)) + ' times':
# def my_func(a: str) ->  str(max(3, 5))+'a repeated '  + ' times':

# 	return a*max(x, y)

# # help(my_func)


# print(my_func.__annotations__)




# lamdafunc=lambda x,*args,y,**kwargs:[x,args,y,kwargs]

# print(lamdafunc(1,'xc','cv',y=5555555,s=1,ss=22))




# x=dict([(1,'Jenish'),(2,'Kajal'),(3,"Pakhe")])
# for z in x.items():
#     print(z)
# # print(x)
# print(type(x))

def return_fucnt_lamda(x,fn):
    return fn(x)

z=return_fucnt_lamda(9,lambda x:x**2)
print(z)
print("---------------------------------------------------")



def func3(fn,*args,**kwargs):
    return fn(*args,**kwargs)

printer=func3(lambda x,y:x+y,1,2)
print(printer)

print("---------------------------------------------------")



'Sorting'


l=[1,2,4,323,23,2,232,32]
print(sorted(l))

print("---------------------------------------------------")

l=['A','a','s','F']
print(sorted(l))
print("---------------------------------------------------")

'Ascii value of order of A'
print(ord("A"))

print(ord('a'))

print("---------------------------------------------------")

'Sorting on the basis of the uppercase values'
l=['A','a','s','F']
print(sorted(l,key=lambda x:x.lower())) 
print("---------------------------------------------------")



'for real number, automatic sorting doesent happen so you need to insert a key function to sperate the type'
print(sorted([3+2j,1-2j,6+4j,-1 + 9j, 2 - 77j,31 - 25j, 40 - 311j,72 + 11j],key=lambda x:(x.real)**2+(x.imag)**2))

print("---------------------------------------------------")

'Sorting names on the basis of last characteres'
print(sorted(['Jenish','Rosha','Roji','Mahesh','Indu','Kajal'],key=lambda x:x[-1]))


print("---------------------------------------------------")
Day=lambda today:today+1

print(f"Day{Day(0)} of #100DaysofCoding")

'shuffleing list using RANDOM'

import random
numList=[1,2,3,4,5,6,7,8,9]

print(sorted(numList,key=lambda numList:random.random()))


''' we define a variable Money in the global namespace. Within the function Money,
 we assign Money a value, therefore Python assumes Money as a local variable. However, 
 we accessed the value of the local variable Money before setting it, so an UnboundLocalError is the result. 
 Uncommenting the global statement fixes the problem.'''

Money = 2000
def AddMoney():
   # Uncomment the following line to fix the code:
#    global Money
   Money = Money + 1

print (Money)
AddMoney()
print (Money)