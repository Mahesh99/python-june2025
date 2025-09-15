# OOP - Object-Oriented Programming

"""
tobj <-- Employee("John", 30, 50000, "123 Main St")
tobj.name="John"
tobj.age=30
tobj.salary=50000
tobj.address="123 Main St"
e1=tobj

Class - blueprint for creating objects
      - instance variables and methods(functions)
      - attributes/properties and behaviour
Object - instance of a class
__init__ - constructor - initializes instance variables

"""

# class definition

class Employee:
    def __init__(self, name, age, salary, address):
        # instance variables
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

class Car:
    tyres = 4  # class variable / static variable

    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color

    def car_details(self):
        return f"Make: {self.make}, Model: {self.model}, Color: {self.color}"

    def repaint(self, new_color):
        self.color = new_color
        return self.color

    @staticmethod
    def print_tyres():
        print(Car.tyres)
    

c1 = Car("Land Rover", "Defender", "olive green")
print(c1.car_details())

c2 = Car("Tata", "Nexon", "red")
print(c2.car_details())

print(Car.tyres)
c1.print_tyres()  # calling static method without creating object


# utility class
# @staticmethod is a decorator
# what is a static method?
# a staic method is a method that belongs to the class rather than the object of a class
# a static method can be called without creating an instance of the class
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    def divide(a, b):
        if b == 0:
            return "Cannot divide by zero"
        return a / b

print(MathUtils.add(10, 5))
print(MathUtils.subtract(10, 5))
print(MathUtils.multiply(10, 5))
print(MathUtils.divide(10, 5))
# m1=MathUtils()
# m1.add(10,5)


class HumanBeing:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def introduce(self):
        print(f"Hi, I'm {self.name}, and I'm {self.age} years old.")

class SuperHero(HumanBeing):
    def __init__(self,name,age,power):
        super().__init__(name,age)
        self.power=power
    def show_power(self):
        print(f"My super power is {self.power}!")
    # here introduce() is overriding superclass introduce() method
    def introduce(self):
        print(f"Hi, I'm {self.name}, and I'm {self.age} years old. My super power is {self.power}!")


# h1=HumanBeing("Alice",25)
# h1.introduce()

sh1=SuperHero("Batman",36,"High Intelligence and advanced gadgets")
sh1.introduce()
sh1.show_power()
