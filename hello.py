# print() is a built-in function
print("Hello world")
print("Welcome to Pramanicus Academy")
print(3+5)
print(10-5)
print(10*5)
print(10/5)

# There are 2 types of comments
# 1.single line comment(#)
# 2.multi-line comment(''' or """)

"""
this is
a 
multi-line
comment
"""

print(5//2)
print(5%2)
print(5**2)

a=10
b=20
#2wt=10
weight=10
print(a,b)
current_temp=28
c=100

match_score = 247
overs = 48
run_rate = match_score / overs
print(run_rate)

#match_score = match_score+4
match_score+=4
match_score-=6

print(match_score)


# Data types
# Integer , float, boolean

a=10
print(type(a))
b=1.1
print(type(b))
c="hello"
print(type(c))
print(type(7))

# type conversion
# int(),float()
# used to convert from one type to other type
# str to int or float
k="45"
j=5
l="1.1"
print(int(k)+j+float(l))
# print(int(l))
m=int(k)
print(type(m),type(k))

z=True
y=False
print(type(z))

r=5>4
print(r)

# Comparison or Relational operator
# >,<,>=,<=,==,!=

print(5<4)
print(5==4)
print(5>=4)
print(5<=4)
print(5!=4)

# logical operators
# and, or, not
# 1-True, 0-False
# print(True+True+False)
print("-------------")
print(True and True)
print(False and True)
print(True and False)
print(False and False)
print("-------------")
print(True or True)
print(False or True)
print(True or False)
print(False or False)
print("-------------")
print(not True)
print(not False)
print("-------------")

age=20
salary=20000
print(age>=18 and salary>=30000)