# Python Object Oriented Programming

class Employee:
    pass  # because classes cant be empty


emp1 = Employee()
emp2 = Employee()

print(emp1)
print(emp2)

emp1.email = "kabuza@mail.com"
emp1.pay = 200000

emp2.email = "shazam@jam.com"
emp2.pay = 150000
print(f"Employee 1: {emp1.email}")
print(f"Employee 2: {emp2.email}")


# To make them easier make use of dunder init
# https://www.tutorialspoint.com/python/python_classes_objects.htm#:~:text=Instance%20%E2%88%92%20An%20individual%20object%20of,instance%20of%20the%20class%20Circle.&text=Object%20%E2%88%92%20A%20unique%20instance%20of,and%20instance%20variables)%20and%20methods.
# Go through the link aswell

class Employee:
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary
        self.email = self.first+'.'+self.last.lower()+'@company.com'

    def printer(self):  # self must be there because instance is passed on its own automatically
        return self.first, self.last, self.email


emp1 = Employee('Katana', 'Master', 30000)
emp2 = Employee("Sakura", "Bloom", 400000)
# while calling a method we need () because the instance is passed on its own
print(emp1.printer())
print(emp2.printer())

# we can also do the following by calling the class but the instance needs to be passed
print(Employee.printer(emp2))
print(Employee.__dict__)
