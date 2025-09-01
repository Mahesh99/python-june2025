
# n=int(input("Enter a number: ")) # 5
# 4! -> 4*3*2*1 = 24
# 5! -> 5*4*3*2*1 = 120

# factorial using for loop
# f=1
# for i in range(1,n+1):#i=5,f=120
#    f=f*i

# print(f)


# factorial using recursion
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

n=int(input("Enter a number: ")) # 0
print(factorial(5))


"""
factorial(5)
if 5==0:
    return 1
else:
    return 5*factorial(4)

factorial(4):
if 4==0:
    return 1
else:
    return 4*factorial(3)

factorial(3):
if 3==0:
    return 1
else:
    return 3*factorial(2)

factorial(2):
if 2==0:
    return 1
else:
    return 2*factorial(1)

factorial(1):
if 1==0:
    return 1
else:
    return 1*factorial(0)

factorial(0):
if 0==0:
    return 1

"""