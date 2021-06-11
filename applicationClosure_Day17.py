def counter(intial_value=0):
    def inc(increment=1):
        nonlocal intial_value
        intial_value += increment
        return (intial_value)
    return inc


# print(counter())
counter1 = counter()
print(counter1())
counter1()
print(counter1())


########################
def counter(fn):
    cnt = 0

    def inner(*args, **kwargs):
        nonlocal cnt
        cnt += 1
        print(f"function named :{fn.__name__} has been called {cnt} times")
        return fn(*args, **kwargs)
    return inner


def add(a, b):
    return a+b


def mult(a, b):
    return a*b


# not passing the args of add because counter1 only takes one argument and that is the function
counter1 = counter(add)
print(counter1(1, 33))
print(counter1(4, 4))

print(counter1.__code__.co_freevars)
counter2 = counter(mult)
print(counter2(2, 2))
print(counter2(3.5, 6))

'we can do the following and store the counter in a dict'
counter = dict()


def outer(fun):
    cnt = 0

    def inner(*args, **kwargs):
        nonlocal cnt
        cnt += 1
        # this might seem like we are assigning value to counter and it would be a local variable but its not , instead we are just changing its content which is different
        counter[fun.__name__] = cnt
        return fun(*args, **kwargs)
    return inner


def add(a, b):
    return a+b


def mult(a, b):
    return a*b


counter1 = outer(add)
print(counter1(1, 2))
print(counter)
counter2 = outer(mult)
print(counter2(3, 4444))
print(counter)

'''
Of course this relies on us creating the counters global variable first and making sure we are naming it that way, so instead, we're going to pass it as an argument to the counter function:'''


def counter(fn, counters):
    cnt = 0

    def inner(*args, **kwargs):
        nonlocal cnt
        cnt = cnt + 1
        counters[fn.__name__] = cnt  # counters is nonlocal
        return fn(*args, **kwargs)

    return inner


func_counters = dict()  # initializing the dict
counted_add = counter(add, func_counters)
counted_mult = counter(mult, func_counters)

# We can now call our functions:
for i in range(5):
    counted_add(i, i)

for i in range(10):
    counted_mult(i, i)

print(func_counters)

# Of course, we don't have to assign the "counted" version of our functions a new name - we can simply assign it to the same name!


def fact(n):
    product = 1
    for i in range(2, n+1):
        product *= i
    return product


fact = counter(fact, func_counters)
fact(4)
print(func_counters)
# Notice, how we essentially added some functionality to our fact function, without modifying what the fact function actually returns.
