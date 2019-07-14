# Python object oriented programming
# Lesson 1 : Classes and Instances

# creating classes. Difference between a class and an instance of a class. 

class Employee:
    def __init__(self, first, last, pay):
        # set instance variables
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '_@company.com'

    def fullname(self):
        return '{} {}'. format(self.first, self.last)


# use 'pass' to skip a class
# A "class" is a blueprint for creating "instances"

emp_1 = Employee('Venkat', 'Rajgopal', 50000)
emp_2 = Employee('Test', 'User', 60000)

# print(emp_1.email)
# print(emp_2.email)

# print(emp_2.fullname())


# Using class name itself
emp_1.fullname()
print(Employee.fullname(emp_1))