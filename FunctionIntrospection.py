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