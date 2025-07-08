text="Pramanicus Academy"
text2='Pramanicus Academy'
print(type(text))
print(type(text2))

text3="""this
is a
multiline
string"""

print(text3)
quotation = "\"Knowledge is power\""
quotation2 = '"Knowledge is power"'
print(quotation)
print(quotation2)

response = 'if you think it\'s  "good" then we will go for it'

# string operations
# +(concatenation), *(repetition)
fname="Christopher"
lname="Nolan"
full_name=fname+" "+lname
print(full_name)
print(lname*5)

rs=lname*5
print(rs)

a="hello"
b="world"
c=a+"world"+"hi"
print(c)

#len() function
# returns the number of characters in a string
l=len(a)
print(l)
print(len(c))

# accessing the characters in a string
# using index
# start from 0
# h  e  l  l  o
# 0  1  2  3  4 <-- index
#-5 -4 -3 -2 -1 <-- neg index
print(a[4])
print(a[-1])


text="Pramanicus Academy Pramanicus AcademyPramanicus Academy2"
ind=0
print(text[ind])
ind2=len(text)-1
print(text[ind2])
print(len(text))

print(text[-1])

#slicing
#var[start:end] end is exclusive
g="hello world"
#  012345678910
p1=g[6:8]#lo wo
print(p1)

p2=g[:8]
print(p2)

p3=g[3:]
print(p3)

p4=g[:]
print(p4)

#step
#var[start:end:step]
g="helloworld"
print(g)
print(g[0:8])
print(g[0:8:2])
print(g[0:8:3])
print(g[::3])
rev=g[::-1]
print(rev)