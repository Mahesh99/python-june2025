# if
# if battery is on low, notify user to charge

battery = 90

if battery <= 20:
    print("Battery is low. Please connect the charger")
    print("Please connect the charger")

print("This line is executed always")


# if else
# print if n number is even or odd

n = 32

if n%2 == 0:
    print(str(n) + " is even")
else:
    print(str(n) + " is odd")

print("This line always executes")


per=90

if per>=90:
    print("Grade-A")
elif per>=80:
    print("Grade-B")
elif per>=70:
    print("Grade-C")
elif per>=60:
    print("Grade-D")
else: #else is not mandatory to write this if elif ladder
    print("Grade-F")

print("Hi")

if 'hello':
    print("checking if zero evaluates true")

print()
a = 9
if a%3 == 0:
    if a%5 == 0:
        print(str(a),"is a multiple of 3 and 5")
    else:
        print("Not a multiple of 3 and 5")
        # if True:
        #     print("hi")
    print("hello")
else:
    print("Not a multiple of 3 and 5")


print()
# Greatest of 3 numbers
# all numbers should not be same
# a=int(input("Enter a:"))
# b=int(input("Enter b:"))
# c=int(input("Enter c:"))
# if a>b and a>c:
#     print("a is greater")
# elif b>c:
#     print("b is greater")
# else:
#     print("c is greater")


print()
# Loops
# to execute the same code multiple times we use loops
# for, while

# for loop
# range() is a function
# range(start,end,step)
# range(10)-end(start=0)
# range(1,11)-start,end
# range(1,11,2)-start,end,step

for i in range(10):
    print("hello")

for i in range(10):
    print(i)

for i in range(1,11):
    print(i)

for i in range(1,11,2):
    print(i)

for i in range(2,11,2):
    print(i)

#3,4,5,6,7,8,9,10,11,12
for i in range(3,31,3):
    print(i)

#3x1=3
#3x2=6
#3x3=9
for i in range(3,31,3):
    print(f"3x{i//3}={i}")

for i in range(5,31,5):
    print(i)
for i in range(5,21,3):
    print(i)
for _ in range(4):
    print(1)

# string, lists, tuple, set, dictionary

numbers = [1,2,3,5,7,8]
# example 1
for n in numbers:
    print(n)

marks=[11,21,22,23,17,16,14]
per=[]
print('--------------------')
for i in marks:
    p=i/25*100
    per.append(p)
    print(p)

print(per)

s="Prmanicus Academy"
s="     "
for c in s:
    print(c)

# exercise 4

# GUESSS THE NUMBER

# there is a given_num variable with some random integer value
# Take a number as input from the user 
# print "You guessed right!!" if he enters the same number
# else print "You guessed wrong. Try again!!"
# n = 32

# if n%2 == 0:
#     print(str(n) + " is even")
# else:
#     print(str(n) + " is odd")




# given_num=13
# inp=12 # ask user to guess the number and take it as input

i=0
while i<=5:
    print(i)  
    i+=1  

i=-1
while i<=3:
    print(i)  
    i+=1  

# i=5
# while True:
#     print(i)  
#     i-=1  

i=5
while False:
    print(i)  
    i-=1  
print("Hi")

l=[3,4,5,6,7]
while l:
    e=l.pop()
    print(e)

# break and continue

# 16
# a number is prime if it has only 2 factor 1 and itslef
# 1 and 16
# 2,3,4,5,...14,15

# n=int(input("Enter a number"))
n=10
isprime=True
for i in range(2,n):
    if n%i==0:
        isprime=False
        break
    
if isprime==True:
    print("Number is prime")
else:
    print("Number is not prime")


for i in range(10):
    print(i)
    if i==5:
        break

for i in range(10):
    break
    print('hi')

for i in range(2,8):
    print(i)
    if i==2:
        break
# break-whenever a break statement is executed the control will come out of the loop and execute follwing statements
# continue - skips current iteration and goes to next iteration

for i in range(10):
    if i==4:
        continue
    print(i)

for i in range(10):
    if i==9:
        continue
    print(i)

for i in range(10):
    if i==9 or i==5:
        continue
    if i==8:
        break
    print(i)