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

