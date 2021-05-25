# study docs here https://docs.python.org/3/library/inspect.html
#https://drive.google.com/file/d/1PU9Yo8yT3dy1sRC-nAjGcqLDUPt5eZdS/view?usp=sharing
'''The inspect Module import inspect

ismethod(obj) isfunction(obj) isroutine(obj) and many others...

What's the difference between a function and a method?
Classes and objects have attributes – an object that is bound (to the class or the object)

def my_func():
pass
def MyClass:
def func(self):
pass

my_obj = MyClass()

ismethod(my_func) → False
isfunction(my_func) → True

ismethod(my_obj.func) → True
isfunction(my_obj.func) → False

An attribute that is callable, is called a method

func is bound to my_obj, an instance of MyClass

isroutine(my_func) → True
isroutine(my_obj.func) → True'''




def myFunc(x,y,/,kw):
    """/ indicates that before this only postional arguments can exist no keyword arguments"""
    print(x)
    print(y)
    print(kw)


print(help(myFunc))
myFunc.category="TestBenchmark"

print(myFunc.category)

print(dir(myFunc))


myFunc(1,2,kw=4)






def myFunc(x,y,*,kw):
    '''* indicates that after star no postional arguments can exist only keword only arguments'''
    print(x)
    print(y)
    print(kw)

myFunc(1,2,kw=114)

#You can see this comment due to inspect.getcomment and also sub commenting learn that
def funcIntrospection(a:'mandatory postiotinal arguement',
b:"mandatory postiotional argument with an default arguments"=9,
c=2,
*args:"have extra postitional arguments here",
d,
e=22,
f=33,
**kwargs:"Provide all extra keyword only arguments here")->"definately does nothing":
    """This function does nothing however contian various parameters"""
    i=100
    j=200

print(funcIntrospection.__doc__)
print(funcIntrospection.__annotations__)

def passFunc(f):
    print(f.__name__)

passFunc(funcIntrospection)

print(f"Fucntional defaults are {funcIntrospection.__defaults__}")
print(f"\nFucntional keywordonly_defaults are {funcIntrospection.__kwdefaults__}")
print(funcIntrospection.__code__)
print(f"\nThe code attribute can be used as the following {dir(funcIntrospection)}")
print(f"\nlist of variabales that exist inside the fucntion attrinute obtained through __code__ is {funcIntrospection.__code__.co_varnames}\n")
# print(funcIntrospection.__name__)


import inspect
from inspect import isfunction,ismethod,isroutine, signature


class myClass:
    def __init__(self) -> None:
        pass

    def fu():
        pass

print(isfunction(myClass.fu))
print(ismethod(myClass.fu))

#but if u create an instance it wont be the same because the function will be bound to the classes instance

instanxe=myClass()
print(isfunction(instanxe.fu))
print(ismethod(instanxe.fu))


print("\n We can also obtain the source code of a fucntion throught the ispect module \n")
print(inspect.getsource(funcIntrospection))



print(inspect.getmodule(funcIntrospection))

print("\n We can also get the comments preeceding a certain code from the function using isnpect.getcomment\n")
print(inspect.getcomments(funcIntrospection))



print("\n Learning Signature object\n")
print(dir(inspect.signature))
# print(type(inspect.signature))

print(inspect.signature(funcIntrospection))
sig=inspect.signature(funcIntrospection)
print("")


print(sig.parameters)
print("")
for param in inspect.signature(funcIntrospection).parameters.values():
    print("Name:",param.name)
    print("Default:",param.default)
    print("Annotation:",param.annotation)
    print("Kind:",param.kind)
    print("--------------------------------------------------")


#Study DOC here https://docs.python.org/3/library/inspect.html