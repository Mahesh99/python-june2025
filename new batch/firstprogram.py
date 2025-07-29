#print("Hello world")
print("Welcome to Pramanicus Academy")
print("1+2")
print(1+4)
print(5-4)
print(5*4)
print(10/4)
print(2314*34)
print(12%3)
print(12%5)
print(5%15)
print(10//5)
print(10**2)
print(5**2)
print(2**3)

a=1
b=2
print(a+b)
c=a+b
print(c)

c=29
f=1.8*c+32 # temperature conversion formulae
print(f)

"""
cricket_score=141

temp_in_c=29
temp_in_f=84
    
print(temp_in_c)
"""
# with=20

# Assignment operator
# =, +=, -=, *=, /=, %=, //=, **=

a=1
# a=a+2
a+=2 #3
print(a)
a-=1 #2
print(a)
a*=3 #6
print(a)
a/=6 #1
print(a)
a=3
a**=3 
print(a)


# data types
# basic - int, float, string, boolean
i=10
f=3.1
s="hello"
b=True # False
print(type(i))
print(type(f))
print(type(s))
print(type(b))
print(type(12))
v=type(12)
print(v)

# type conversion
# int(), float(), str() - functions
temp="29.5"
newtemp="30"
print(int(newtemp)-float(temp)) #"30"-"29.5" --> 30-29.5
a=int("15")
print(type(a))
print(type("15"))

# string operations
# +(concatenation),*(repition)
f="pramanicus"
l="academy"
fn=f+l
print(fn)
msg="hi"
print(msg*5)


tp=29.5
stp=str(tp) #"29.5"
print(type(tp),type(stp))
print("temperature is "+str(tp))

print(int(3.4))
print(int("3"))
# print(int("3.4"))

print(float(3.4))
print(float("3"))
print(float("3.4"))
# print(float("abc"))


# Comparison operators
# >,<,>=,<=,==,!=
print(2>3)
print(2<3)
print(2>=3)
print(2<=3)
print(2==3)
print(2!=3)
a=10
b=20
print(a>b)
print(a>5)

print(type(2>3))


# logical operators
# and, or, not
# True - 1, False-0

print(True and True)
print(True and False)
print(False and True)
print(False and False)

print()
print(True or True)
print(True or False)
print(False or True)
print(False or False)

print()
print(not True)
print(not False)
b=True or True
print(type(b))

age=17
salary=25000
# age should be 18 or above
# salary should be 20000 or above
print(age>=18 and salary>=20000)

tp=input("Enter the temperature:") #"30"
print("temperature is "+tp)

