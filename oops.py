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




# Magic methods or dunders(double underscore methods)
class Employee:
    # this method is called only once i.e when we create an object 
    def __init__(self,name,age,salary,address):
        # instance/object variables
        self.name=name
        self.age=age
        self.salary=salary
        self.address=address
    
    def update_salary(self,newsalary):
        self.salary+=newsalary
    def print_details(self):
        print(f"Name:{self.name}\nAge:{self.age}\nSalary:{self.salary}\nAddress:{self.address}")
    def __str__(self):
        return f"{self.name}--{self.salary}"
    def __add__(self,obj2):
        # return f"{self.name}--{obj2.name}"
        return self.salary+obj2.salary
    def __len__(self):
        return 1


e=Employee("Hari",30,40000,"Uppal")
e2=Employee("Ravi",25,25000,"Amberpet")
print(e)
print(e2)
print(e+e2)
print(len(e))



print()
print()

l=[4,1,5,7,9]
itr=iter(l)
print(type(itr))

# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))

# a=next(itr)
# b=next(itr)
# c=next(itr)
# d=next(itr)
# print(a,b,c,d)
# e=next(itr)

print()
print()

class MyIterator:
    def __init__(self,n):
        self.n = n

    def __iter__(self):
        return self
        
    def __next__(self):
        if self.n == 0:
            raise StopIteration()
        temp = self.n
        self.n -= 1
        return temp
    
miter = MyIterator(6)
i = iter(miter)
print(next(miter))
print(next(miter))
print(next(miter))
print(next(miter))
print(next(miter))
print(next(miter))
# print(next(miter))

miter = MyIterator(10)
for i in miter:
    print(i)

print('hello')

print()
print()

#Generators
def my_range(n):
    count = 0
    while count < n:
        yield count 
        count += 1


# for i in my_range(4):
#     print(i)
# for i in range(4):
#     print(i)

my = my_range(4)
print(next(my))
print(next(my))
print(next(my))
print(next(my))
# print(next(my))

# 0 1 2 3 2 1 0
def my_special_range(n):
    count = 0
    while count < n:
        yield count 
        count += 1
    count -= 2
    while count >= 0 :
        yield count 
        count -= 1

for i in my_special_range(4):
    print(i)




# print()
# print()
# #generator expressions
# l=[x*3 for x in range(1000)]
# g=(x*3 for x in range(2))

# for i in g:
#     print(i)

# print(next(g))
# # print(next(g))
# # print(next(g))




# Exercise - Iterator

# class WordIterator:
#     def __init__(self,sentence):
#         self.index=0
#         self.wlist=sentence.split()
#     # write function __iter__ and __next__
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         pass
    

# wi=WordIterator("Welcome to python programming classes")  

# for i in wi:
#     print(i)
