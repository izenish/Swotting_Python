
import math
print("______________________________________________Day 6___________________________________________________________________")

mapvalue=map(math.factorial,range(10))
for x in mapvalue:
    print(x)      #because map returns iterator not list so we need to convert it into a list to print it beforehand




'Reducing function is also called as aggrefators and folding functions'

l=[5,6,3,56,100]
max=l[0]
for x in l:
    if max<x:
        max=x

print(max)
print("The result of the above function in reduced format is as follow\n")
def reducedFunc(fn,l):
    result=l[0]
    for x in l[1:]:
        result=fn(result,x)
    print(f"{result} is the maximum among the list {l}")

reducedFunc(lambda x,y:x if x>y else y,l)

'Python has its own builtin reduce functions'
import functools

l=[0,'',None,100]

print(functools.reduce(lambda x,y:bool(x) or bool(y),l))
'Reduce needs to be imported from functools but not "any"'
print(f"THe value is checked using any {any(l)}")

l=[1,2,3,4]

'Reduce also has an initializer'
print(functools.reduce(lambda x,y:x+y,l,100))  #here initializer is 100 , its equivalent to initializing l[0]=100 then the remaining l follows