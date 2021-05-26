'Callable are those objects that can be called using an () operator and THEY MUST ALWAYS RETURN A VALUE'
'Use builtin function callable() to check if its callable or not'
print(callable(print))
print(callable('abc'.upper))
print(callable(10))


print("")

def func_callable():
   x = 3
   y = 5
   z = x^y
   return z
# an object is created of Geek()
res = func_callable
print(callable(res))
# print(res)
# Call and use the function
final_res=func_callable()
print(callable(final_res))


# Class instances may be callable:

class MyClass:

    def __init__(self):

        print('initializing...')

        self.counter = 0

    

    def __call__(self, x=1):

        self.counter += x

        print(self.counter)

my_obj = MyClass()
print(callable(my_obj.__init__))