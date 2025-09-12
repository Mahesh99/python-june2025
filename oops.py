# OOP - Object-Oriented Programming

"""
tobj <-- Employee("John", 30, 50000, "123 Main St")
tobj.name="John"
tobj.age=30
tobj.salary=50000
tobj.address="123 Main St"
e1=tobj
"""

# class definition

class Employee:
    def __init__(self, name, age, salary, address):
        self.name = name
        self.age = age
        self.salary = salary
        self.address = address
    
    def emp_details(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}, Address: {self.address}"
    
    def increment_salary(self, increment):
        self.salary += increment
        return self.salary


# creates an object
e1 = Employee("John", 30, 50000, "123 Main St")

print(e1.name)
print(e1.age)
print(e1.salary)
print(e1.address)
e1.age = 31  # updating age
print(e1.age)
print(e1.emp_details())
us=e1.increment_salary(5000)
print(us)

e2 = Employee("Patrick Jane", 28, 60000, "456 Elm St")
print(e2.name)
print(e2.age)
print(e2.salary)
print(e2.address)
e2.increment_salary(7000)

# s="hello"
# s.upper()