# print() is a built-in function
print("Hello student!") # i'm printing hello students
print("Welcome to Pramanicus Academy")

'''
print(2+4)
print(121+555)
print(33-30)
print(2*5)
print(10/2)
'''
print(15/2)
print(15//2)
print(15%2)
print(15%4)
print(15%5)
print(15%3)
print(3**2)
print(2**2)
print(4**2)
print(2**3)

a=1
b=2.5
c="hi"
print(a)
d=a+b
print(d)
# print(e)
print(d+5)
# print(d+c)
print("1+2")

# 2myvar=30
myvar2=30
print(myvar2)
# and=10
# print(and)
_i=20
print(_i)
student_marks=79
cricket_score=300
weather_today="Raining"

# del a
# print(a)

# assignment operators
"""
=
+=
-=
*=
/=
%=
//=
**=
"""
cs=300
# cs=cs+4
# cs=cs+6
cs+=4
cs+=6
cs-=6
j=5
j%=2
print(j)

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


# type conversion
# int(), float(), str()
temp="29.5"
newtemp="30"
print(float(temp)-int(newtemp))
t=float(temp)
print(type(temp))
print(type(t))
#float("29.5") float(2)
#int("29.5") int(2.5) int("29")
print(int("29"))
print(int(2.5))

# string operations
# +(concatenation),*(repition)
f="pramanicus"
l="academy"
fn=f+l
print(fn)
msg="hi"
print(msg*5)

tp=29.5
stp=str(tp)
print(type(tp),type(stp))
print("temperature is "+str(tp))

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

print()
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

age=18
salary=25000
# age should be 18 or above
# salary should be 20000 or above
print(age>=18 and salary>=20000)

tp=input("Enter the temperature:") #"30"
print("temperature is "+tp)