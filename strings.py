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

# int(), float()
# str() is used to convert number types(int,float) to string
print(int("12")+4)
print(float("12.1")+4)
price=2000
fprice=price-(2000*10/100)
print("Price after 10% discount is "+str(fprice))
print("hi"+str(12))
a=str(12) #"12"
print(type(a))
print(type(12))

a=1
b=1.1
c="hi"
e=str(a)
f=str(b)
print(type(a),a)
print(type(b),b)
print(type(c),c)
print(type(e),e)
print(type(f),f)

# string methods
# lower(), upper(), 
text="PRAMANICUS ACADEMY"
t2=text.lower() 
print(text,t2)
text2="hello world"
t3=text2.upper()
print(text2)
print(t3)

t4="hi".upper()
print(t4)

print("hi".upper())
print(text2.title())
print(text2.capitalize())
print(text.capitalize())


#count()

print("Where there’s smoke, there’s fire".count(' ther'))
print("Where there’s smoke, there’s fire".count('h'))
print("Where there’s smoke, there’s fire".count('h',0,12))
print("Where there’s smoke, there’s fire".find('h',4,12))
print("Where there’s smoke, there’s fire".find('there'))
print("Where there’s smoke, there’s fire".find('hi'))
print()
print("Where there’s smoke, there’s fire".index('h',4,12))
print("Where there’s smoke, there’s fire".index('there'))
# print("Where there’s smoke, there’s fire".index('hi'))

# islower()
text2="hello world"
text="PRAMANICUS ACADEMY"
print(text2.islower())
print(text2.isupper())
print(text.isupper())
print("hi123".isalnum())
print("hi123_".isalnum())
print("hi123+".isalnum())
print("hi123+".isdigit())
print("123".isdigit())

#format(),capitalize()

name = "ARJUN"
favourite_color = "Navy Blue"
sentence = "{}'s favourite color is {}"
# print(sentence)
print(sentence.format(name,favourite_color))
print(sentence.format("hi","hello"))


# List
l=[1,2,3,4]
friends=["pranav","ashfaq","manuraj","likitha","sathvika"]
print(type(l))
print(l)
n=len(l)
print(n)
print(len(friends))
print(friends[2])
print(friends[4])
print(friends[-1])
boys=friends[0:3]
girls=friends[3:]
print(boys)
print(girls)
print(friends[3])
friends[3]="ruthika"
print(friends)

l=[1,2,3,4]
l[0]=10
print(l)
l[2]=20
print(l)

# membership operators
# in, not in
print(1 in l)
print(1 not in l)
print("rishi" in boys)
name="hari"
print(name in boys)
res="sai" not in boys
print(res)

# min(), max(), sum(), len(), join()
l=[1,2,3,4]
mn=min(l)
mx=max(l)
sm=sum(l)
print(mn,mx,sm)

l2=["seperate","all","list","strings","with","specified","string"]
sent=" ".join(l2)
print(sent)