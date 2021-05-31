from FunctionIntrospection import myClass
import operator
import functools
print([x for x in dir(operator)])

'Builtin functions to reduce unnecessary lambda functions'

print(operator.add(99,1))  #addition
print(list(map(operator.neg,range(9)))) #negation
print(operator.truediv(3,2))
print(operator.floordiv(3,2))

l=[1,2,3,4]
print(functools.reduce(operator.mul,l)) #reduced than reduce(lambda x,y:x*y,l)

print(operator.lt(2,9)) #less than
print(operator.is_(1,10)) #is_ to remove conflict from is builtin


'getters and setters'
my_list=[1,2,3,5]
print(operator.getitem(my_list,2)) #equivalent to my_list[2]
operator.setitem(my_list,2,222) #appending
operator.delitem(my_list,1)
print(my_list)

'itemgetter acts as a partial function'
f=operator.itemgetter(2) #returns a function
print(type(f))
print(f(my_list)) #->f=operator.getitem(mylist,2)
print(f('Jenish'))

'can have more than one argument'

f=operator.itemgetter(2,3,4) #returns a function
print(f('the quick brown fox jumped over the lazy brown fox'))

class MyClass:
    def __init__(self):
         self.a=10
         self.b=20
         self.c=30

    def method_underclass(self):
        print("Method is currently processign")

obj=MyClass() #instance
print(obj.a)

obj.method_underclass #this returns the method
print(obj.method_underclass)
obj.method_underclass() #this calls the method

'attribute getter takes a string as an argument and returns a callable'
f=operator.attrgetter('a')
print(f(obj))

r_i=[4-20j,3+3j,44-3j]
print(sorted(r_i,key=operator.attrgetter('real'))) #attrgetter('real') returns a callable that needs a value which is then provided by the key
'its the same as using sorted(r_i,key:lambda x:x.real)'


second_instance=MyClass()
f=operator.attrgetter('method_underclass')
f(second_instance)() #f(second_instance) returns the method to call it we use ()

'alternatively we can use methodcaller'
f=operator.methodcaller('method_underclass')
f(second_instance) #because the method was called not returned


'Also study standard operator as functions'