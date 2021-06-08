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
