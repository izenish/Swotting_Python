# LAB -1: Family Tree

import json
from logpy import Relation, facts, run, conde, var, eq

#Define a function to check if x is the parent of y.
#logic: if x is the parent of y, then x is either the father or mother
def parent(x,y):
    return conde([father(x,y)],[mother(x,y)])

#define a function to check if x is the grandparent of y.
#logic: if x is the grandparent of y, then the offspring of x will be 
#the parent of y.
def grandparent(x,y):
    temp=var()
    return conde((parent(x,temp), parent(temp,y)))

#define a function to check if x is the sibling of y
#logic: if x is the sibling of y, then x and y will have same parents.
def sibling(x,y):
    temp=var()
    return conde((parent(temp,x), parent(temp,y)))

#define a function to check if x is y's uncle
#logic: if x is y's uncle, then y's grandparents will be the same as x's parents.
def uncle(x,y):
    temp=var()
    return conde((father(temp,x),grandparent(temp,y)))



if __name__=='__main__':
    father=Relation()
    mother=Relation()
    
    with open('LAB1/relationships.json') as f:
        d=json.loads(f.read())
        
    #Read the data and add them to our fact base
    for item in d['father']:
        facts(father,(list(item.keys())[0],list(item.values())[0]))
        
    for item in d['mother']:
        facts(mother,(list(item.keys())[0],list(item.values())[0]))
        
    #define the variable x
    x=var()
    
    #let's ask who John's children are.
    name='John'
    output= run(0,x,father(name,x))
    print("\n list of" + name + " 's children:")
    for item in output:
        print(item)
        
    #who is William's mother?
    name='William'
    output=run(0,x,mother(x,name))[0]
    print('\n' + name+ " 's mother:\n" + output)
    
    #who are Adam's parents?
    name='Adam'
    output=run(0,x,parent(x,name))
    print("\n list of" + name + " 's parents:")
    for item in output:
        print(item)
        
    #who are Peter's grandparents?
    name='Peter'
    output=run(0,x,grandparent(x,name))
    print("\n list of" + name + " 's grandparents:")
    for item in output:
        print(item)
        
    #who are Megan's grandchildren?
    name='Megan'
    output=run(0,x,grandparent(name,x))
    print("\n list of" + name + " 's grandchildren:")
    for item in output:
        print(item)
        
    #who are David's siblings?
    name='David'
    output=run(0,x,sibling(x,name))
    siblings=[x for x in output if x!=name]
    print("\n list of" + name + " 's siblings:")
    for item in siblings:
        print(item)
        
    #who are Neil's uncles?
    name='Neil'
    name_father=run(0,x,father(x,name))[0]
    output=run(0,x,uncle(x,name))
    uncles=[x for x in output if x!=name_father]
    print("\n list of" + name + " 's uncles:")
    for item in uncles:
        print(item)
        
        
    #list out all spouses in the family
    a,b,c= var(), var(), var()
    output=run(0,(a,b),father(a,c),(mother,b,c))
    print("\n list of spouses:")
    for item in output:
        print('Husband:',item[0],'<===>Wife:',item[1])
    