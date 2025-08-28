# import modules
# import testt

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


def hello():
    print("Hello, World!")

def greet(name):
    print(f"Hello, {name}!")

def add(a, b):
    c = a + b
    print(f"The sum of {a} and {b} is {c}.")

first_5_primes=[2,3,5,7,11]

if __name__=="__main__":
    add(5, 10)
    hello()
    # primetest()
    print(__name__)