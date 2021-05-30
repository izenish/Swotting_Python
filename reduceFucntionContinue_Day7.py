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
