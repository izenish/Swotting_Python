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
from typing import SupportsAbs
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


# Day20


def timed(fn):
    from time import perf_counter
    from functools import wraps

    @wraps(fn)
    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        elapsed = end - start

        args_ = [str(a) for a in args]
        kwargs_ = ['{0}={1}'.format(k, v) for (k, v) in kwargs.items()]
        all_args = args_ + kwargs_
        args_str = ','.join(all_args)
        print('{0}({1}) took {2:.6f}s to run.'.format(fn.__name__,
                                                      args_str,
                                                      elapsed))
        return result

    return inner


'''
@timed
def calc_recursive_fib(n):
    if n <= 2:
        return 1
    else:
        return calc_recursive_fib(n-1) + calc_recursive_fib(n-2)


print(calc_recursive_fib(9))


@timed
def fib_recursed(n):
    return calc_recursive_fib(n)


print(fib_recursed(10))'''

'''Using Reduce
We first need to understand how we are going to calculate the Fibonnaci sequence using reduce:

n=1:
(1, 0) --> (1, 1)

n=2:
(1, 0) --> (1, 1) --> (1 + 1, 1) = (2, 1)  : result = 2 

n=3
(1, 0) --> (1, 1) --> (2, 1) --> (2+1, 2) = (3, 2)  : result = 3

n=4
(1, 0) --> (1, 1) --> (2, 1) --> (3, 2) --> (5, 3)  : result = 5
In general each step in the reduction is as follows:

previous value = (a, b)
new value = (a+b, a)
If we start our reduction with an initial value of (1, 0), we need to run our "loop" n times.

We therefore use a "dummy" sequence of length n to create n steps in our reduce.'''


@timed
def fib_reduce(n):
    from functools import reduce
    initial = (1, 0)
    dummy = range(n-1)
    fib_n = reduce(lambda prev, n: (prev[0] + prev[1], prev[0]),
                   dummy,
                   initial)
    return fib_n[0]


print(fib_reduce(40))


def logger(fn):
    from datetime import datetime
    from functools import wraps, reduce

    @wraps(fn)
    def inner(*args, **kwargs):
        current = datetime.now()
        print(f"FUNCTION {fn.__name__} was called at {current}")
        return fn(*args, **kwargs)
    return inner


@logger
def sum(a, b):
    return a+b


print(sum(5, 6))

# we can also do the following that is combining the both decorators


@logger
@timed  # this is equivalent to calling sum=logger(timed(sum))
def sum(a, b):
    return a+b


print(sum(5, 60))


# actual logging
def my_logger(org_func):
    import logging 
    logging.basicConfig(filename='Loged_{}.log'.format(org_func.__name__),level=logging.INFO)

    def wrapper(*args,**kwargs):
        logging.info('Ran with args:{}, and kwargs:{}'.format(args,kwargs))
        return org_func(*args,**kwargs)
    
    return wrapper

@my_logger
def fib_reduce(n):
    from functools import reduce
    initial = (1, 0)
    dummy = range(n-1)
    fib_n = reduce(lambda prev, n: (prev[0] + prev[1], prev[0]),
                   dummy,
                   initial)
    return fib_n[0]

print(fib_reduce(99))

