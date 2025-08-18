# 1. right angle triangle star pattern
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
n = int(input("Enter the number of rows: "))
for i in range(1, n + 1):
    print("* " * i)  



# 2. equilateral triangle star pattern
#     * 
#    * *
#   * * * 
#  * * * * 
# * * * * * 
n = int(input("Enter the number of rows: "))
for i in range(1,n+1):
    print(" " * (n - i) + "* " * i)



# 3. sum of digits of a number
def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10)
    
number = int(input("Enter a number: "))
result = sum_of_digits(number)
print(f"The sum of digits of {number} is {result}") 
sum_of_digits(number)




# 4. Palindrome check for a number
n = int(input("Enter a number: "))
t = n
sum = 0

while t > 0:
    digit = t % 10
    sum = sum * 10 + digit
    t //= 10
    
if n == sum:
    print(f"{n} is a palindrome")
else:
    print(f"{n} is not a palindrome")


# 5. Prime number check
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

primetest()

# 6. Even or Odd check

def even_or_odd():
    n = int(input("Enter a number: "))
    if n % 2 == 0:
        print(f"{n} is an even number.")
    else:
        print(f"{n} is an odd number.")

even_or_odd()