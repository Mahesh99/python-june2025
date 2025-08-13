# n=int(input("Enter a number: "))

# is_prime = True
# for i in range(2, n):
#     if n % i == 0:
#         is_prime = False
#         break

# if is_prime:
#     print(f"{n} is a prime number.")
# else:
#     print(f"{n} is not a prime number.")


# functions

# function definition
def primetest():
    n=int(input("Enter a number: "))

    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{n} is a prime number.")
    else:
        print(f"{n} is not a prime number.")


# function call
# primetest()
# primetest()
# primetest()
# primetest()

def hello():
    print("Hello, World!")

hello()
hello()
# primetest()
hello()

# function with parameters
# name is a parameter
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
greet("Bob")
greet("Hari")
# primetest()

# a and b are parameters
def add(a, b):
    c = a + b
    print(f"The sum of {a} and {b} is {c}.")

add(5, 10)
add(20, 30)
# add(100, 200)

def multiply(a, b):
    c = a * b
    return c

result = multiply(5, 10)
print(result)

# default arguments
def greet_user(name="Guest"):
    print(f"Hello, {name}!")

greet_user()
greet_user("Alice")

# default arguments should be at the end
def power(number,exponent=2):
    res = number ** exponent
    return res

print(power(6,3))
print(power(5))
print(power(5, 3))

# variable length of arguments
# args=(1, 2, 3)
def add_numbers(*args):
    total = sum(args)
    return total

print(add_numbers(1, 2, 3))
print(add_numbers(4, 5, 6, 7, 8))

l=[1, 2, 3, 4, 5]

#lst=l
def modify_list(lst):
    lst.append(6)

modify_list(l)
print(l)


def test():
    return "This is a test function."

a=test()
print(a)

print(test())

def test2(a=4):
    print(a)
    # return None

test2()
test2(5)
print(test2(10))

def test3(a, b=5):
    print(a, b)

test3(10)
test3(10, 20)