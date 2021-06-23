import os

print(os.getcwd())
print(os.__file__)


'import antigravity  -> opens a commic on the browser although this is  a builtin import'

'Tuples are immutable'

a=(10,20,30)
b=4,5,6
print(type(a))
print(type(b))
# print(a[1:2])
s=1,2,3,4,5,6,7,77
x,y,*_,z=s #unpacking
print(*_)
print(_)


'remember tuple is immutable but if its contents are mutable then we can mutate that'

london='London','UK',8_700_00
kathmandu='Kathmandu','Nepal',20000
moscow='Moscow',"Russia",12_00_00

cities=[london,kathmandu,moscow]
print(cities)
print(sum([city[2] for city in cities])) #Sum of the population of the cities
# print(0.1+0.2) the o/p isn't 0.3



'Another frequent application of usign tuples as data structures is for returning multiple values from a function.'
from random import uniform
from math import sqrt
from logger import log_this

@log_this
def random_shot(radius):
    '''Generates a random 2D coordinate within the bounds [-radius,radius]*[-radius,radius]
    (a square of area 4) and also determines if it falls within a circle centered at the origin 
    with specidied radius'''

    random_x=uniform(-radius,radius)
    random_y=uniform(-radius,radius)

    if sqrt(random_x**2+random_y**2)<=radius:
        is_in_circle=True
    else:
        is_in_circle=False
    return random_x,random_y,is_in_circle


num_attempts=10000
count_inside=0
for i in range(num_attempts):
    *_,is_in_circle=random_shot(1)
    if is_in_circle:
        count_inside+=1

print(f'Pi is approximately: {4*count_inside/num_attempts}')
