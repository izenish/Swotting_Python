# Decorators and the @ symbol (@ is just used for the convinience)

'''In general, if func is a decorator function, we decorate
another function my_func using:'''

'''

my_func = func(my_func)

This is so common that python provides a convinient way of writing that:


@func
def my_func(..):
    ...function


is the same as writting


def my_func(...):
    ...function


my_func = func(my_func)

'''




from functools import wraps
def counter(fn):
    count = 0

    def inner(*args, **kwargs):  # keeping it generic to accept any kind of argument that was passed into it
        'this is the inner closures doc'
        nonlocal count
        count += 1
        print('Function {0} was called {1} times'.format(
            fn.__name__, count))
        result = fn(*args, **kwargs)
        return result
#    this does help but the arguments passed can't still be changed therefore use wraps from functools
    inner.__name__ = fn.__name__
    inner.__doc__ = fn.__doc__
    return inner


def add(a: int, b: int = 0):
    'adds two values'
    return(a+b)


print(help(add))
print(id(add))

add = counter(add)
print(id(add))
print(help(add))
print(add(1, 3))


def mult(a, b, c, *, d):
    return a*b*c*d


mult = counter(mult)
print(mult(1, 2, 4, d=9))


'we can use the Python way of decorating aswell'


@counter
def my_funct(a: str, i: int):
    return(a*i)


print(help(my_funct))
print(my_funct('ZEAL', 9))

# not exactly what we want so
print(f"The .__name__ of function  my_funct is : {my_funct.__name__}")

'wraps itself is a decorator but takes a function as an argument'


def counter(fn):
    count = 0

    # @wraps(fn)
    def inner(*args, **kwargs):  # keeping it generic to accept any kind of argument that was passed into it
        'this is the inner closures doc'
        nonlocal count
        count += 1
        print('Function {0} was called {1} times'.format(
            fn.__name__, count))
        result = fn(*args, **kwargs)
        return result
    inner = wraps(fn)(inner)  # or could have used @wraps(fn) above
    return inner


def mult(a, b, c, *, d):
    'multiplies the values'
    return a*b*c*d


print(help(mult))
mult = counter(mult)
print(help(mult))
print(mult(1, 2, 4, d=9))
