# help(map)

'Map function'
import math
l1=[5,6,7]
l2=[10,10,10]
print(list(map(math.factorial,l1)))

def adder(x,y):
    return x+y

print(list(map(adder,l1,l2)))
print([x+y for x,y in zip(l1,l2)]) #using list comprehension

'Using lambda function as a subtractor in MAP'
print(list(map(lambda x,y:y-x,l1,l2)))


'Filter'
'''The filter() method filters the given sequence with the help of a function that tests each element in the sequence to be true or not.

syntax:

filter(function, sequence)
Parameters:
function: function that tests if each element of a 
sequence true or not.
sequence: sequence which needs to be filtered, it can 
be sets, lists, tuples, or containers of any iterators.
Returns:
returns an iterator that is already filtered.
'''

def evenChecker(x):
    return True if x%2==0 else False
   

def oddChecker(x):
   return False if x%2==0 else True

print(list(filter(evenChecker,l1)))

print([x for x in l1 if x%2==0])  #using list comprehension   [<expresion1> for <varname> in <iterable> if <expression2>]

print(list(filter(oddChecker,l1)))

print(list(filter(lambda z:z%5==0,l1)))

'''The purpose of zip() is to map the similar index of multiple containers so that they can be used just using as single entity.

    Syntax :
    zip(*iterators)
    Parameters :
    Python iterables or containers ( list, string etc )
    Return Value :
    Returns a single iterator object, having mapped values from all the
    containers.
    '''
'Zip ends at the lowest index for example'

l3=[1,2,3,4]
l4='Kathmandu'
print(list(zip(l3,l4)))
'The above zip stopped at h because the l3 list had only 4 iterables'


'list comprehension is an alternative to map '
'returning square root of a list'
print([x**2 for x in l1])   # [<expression> for <varname> in <iterable>] using list comprehension
# or
print(list(map(lambda x:x**2,l1)))


l5=range(10)
# print(list(filter(lambda x:x<25,list(map(lambda y:y**2,l5)))))
print(list(filter(lambda x:x<25,map(lambda y:y**2,l5))))

print([x**2 for x in l5 if x**2<25])  #using list comprehension





