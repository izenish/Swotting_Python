l=[1,5,63,43,34]
l2=[232323,342342342342343,34]
_max=lambda x,y:x if x>y else y
_min=lambda x,y:x if x<y else y

def greater(l):
    max=l[0]
    for i in l[1:]:
        max=_max(i,max)
    print(f"The max value from the list is {max}")


def lesser(l):
    max=l[0]
    for i in l[1:]:
        max=_min(i,max)
    print(f"The max value from the list is {max}")



greater(l)
lesser(l)

import functools
print(functools.reduce(_max,{11,2323,1}))
print(min(l))   #builtin min function
print(max('pythonx')) #builtin max function

print(all([0,1]))  #all acts as a logical AND operator
print(any({0,1}))  #any acts as a logical OR operator

print(functools.reduce(lambda x,y:x*y,range(1,5+1))) #factorial through reduced function (5+1) because we reduced ZERO 

'Partial is an import from fucntools that is used to reduce the number of arguments intake'

def power(base,exponential):
    return base**exponential

square=functools.partial(power,exponential=2)  

print(f"The square of 12 is {square(12)}")  #the value 12 is passed only to the first positional argument an exponential is 2 by default

cube=functools.partial(power,exponential=3)

print("The cube of {0} is {1}".format(15,cube(15)))

origin=(0,0)
dist_List=[(1,2),(0,3),(3,1)]
dict_inbetween=lambda a,b:(b[0]-a[0])**2+(b[1]-a[1])**2
print("the distance is")
print(dict_inbetween((1,1),origin))
 
'we know the key on sorted method only accepts one variable or key so to reduce the number of variables we use partial'
reduced_key=functools.partial(dict_inbetween,origin)
print(sorted(dist_List,key=reduced_key))