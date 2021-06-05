'Global scopes lies within built-in scopes and each of the modules store em in their own namespace'
'builtins have there own namespace and modules have their own namespace'

#for example 
# print(a) #this throws an error because it looks for print and a on this module's namespace
# but doesn't find any then it searches on the built-in namespace where print is found but not a hence the error

# print=lambda x:'Hello {0}'.format(x)
# s=print("World")
# print(f"The value of print is first checked in the module and since it finds it here it doesnt look in the built in modile {s}")

# a=10
# def func():
#     print(a)
#     a=100

# func()             # UnboundLocalError: local variable 'a' referenced before assignment
'The above error occurs because while compiling func() a is assigned a value so it is now local but the print statement occurs before the assignment it does not know what it is'





#NonLocal scopes are found in between nested functions

def outer_func():
    x="Hello"

    def inner_func():
        x="World"

    inner_func()
    print(x)

outer_func()

#theoutput is Hello because the x inside inner function has a local scope inside it
def outer_func():
    x="Hello"

    def inner_func():
        nonlocal x
        x="World"

    inner_func()
    print(x)

outer_func()



#the output is now World because the nonlocal scope of x inside inner_funct was termed as nonlocal

x = 100
def outer():
    x = 'python'  # masks global x
    def inner1():
        nonlocal x  # refers to x in outer
        x = 'monty' # changed x in outer scope
        def inner2():
            global x  # refers to x in global scope
            x = 'hello'
        print('inner1 (before):', x)
        inner2()
        print('inner1 (after):', x)
    inner1()
    print('outer', x)
outer()
print(x)