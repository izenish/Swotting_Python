'Global scopes lies within built-in scopes and each of the modules store em in their own namespace'
'builtins have there own namespace and modules have their own namespace'

#for example 
# print(a) #this throws an error because it looks for print and a on this module's namespace
# but doesn't find any then it searches on the built-in namespace where print is found but not a hence the error

print=lambda x:'Hello {0}'.format(x)
s=print("World")
print(f"The value of print is first checked in the module and since it finds it here it doesnt look in the built in modile {s}")

a=10
def func():
    print(a)
    a=100

func()             # UnboundLocalError: local variable 'a' referenced before assignment
'The above error occurs because while compiling func() a is assigned a value so it is now local but the print statement occurs before the assignment it does not know what it is'