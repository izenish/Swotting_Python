from time import perf_counter


class Avg:
    def __init__(self):
        self.numbers = []

    def add(self, number):
        self.numbers.append(number)
        total = sum(self.numbers)
        count = len(self.numbers)
        return total/count


a = Avg()
print(a.add(10))
print(a.add(20))
print("________-")


def averager():
    numbers = []

    def add(number):
        numbers.append(number)
        total = sum(numbers)
        count = len(numbers)
        print(total/count)

    return add  # dont forget to return the closure


x = averager()
print(type(x))
x(100)
x(200)


def averager():
    total = 0
    count = 0

    def add(number):
        nonlocal count
        nonlocal total
        total = number+total
        count = count+1
        print(total/count)

    return add


y = averager()
y(12)
y(24)

# Checking the free variables and closure
print(y.__closure__)
print(y.__code__.co_freevars)


start = perf_counter()
for x in [1, 2, 3, 4, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 106, 101010101010101001010]:
    if(x % 2):
        print(x)

end = perf_counter()
print(f"Time elapsed is {end-start}")


class Timer:
    def __init__(self) -> None:
        self.start = perf_counter()

    def elapsed(self):
        print(f"Time elapsed is {perf_counter()-self.start}")


x = Timer()
x.elapsed()  # instead of this we should convert the elapsed to builtin
"""def __call__(self):
           print(f"Time elapsed is {perf_counter()-self.start}")"""

# __call__ is a callable due to which we can just call the above code into x() no need to call x.elapsed()
