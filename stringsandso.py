#strings
# string are created using double or single quotes(" or ')
# to create multiline string use """ or '''
f="pramanicus"
l='academy'
fn=f+l
print(fn)

mls="""this is a
multiline
string"""
print(mls)

quotation = "\"Knowledge is power\""
print(quotation)
#escape character
advice = 'It\'s always good to follow best practices'
# advice = "It's always good to follow best practices"
print(advice)

mls2="this is a \nmultiline\n string"
print(mls2)
# new line character - \n
# escape character - \
# backslash - \\

s="hello\\"
print(s)


f="pramanicus"
# Indexing
#  p r a m a n i c u s
#  0 1 2 3 4 5 6 7 8 9
#-10-9-8-7-6-5-4-3-2-1
print(f[3])
print(f[7])
print(f[9])
print(f[-1])
print(f[-3])

# slicing
# vn[start:end] - end is exclusive
# [1,5)
s="hello world"
s1=s[0:5]
print(s1)
s2=s[6:11]
print(s2)
s3=s[4:7]
print(s3)
s4=s[6:]
print(s4)
s5=s[:5]
print(s5)
s6=s[:]
print(s6)

# step
# vn[start:end:step]
s="hello world"
v=s[0:8:2]
print(v)
v=s[0:8:3]
print(v)
v=s[0:8:4]
print(v)
v=s[::2]
print(v)
r=s[::-1]
print(r)

# string methods
# vn.method_name([arg1[,arg2,..]])
s="hello world"
u=s.upper()
print(u)
l=u.lower()
print(l)
t=s.title()
print(t)
t=u.capitalize()
print(t)
n=s.count('l')
print(n)
n=s.count('L')
print(n)
n=s.count('l',0,5)
print(n)

s="hello world"
n=s.find('wr')
print(n)
n=s.find('o',5)
print(n)
n=s.find('z')
print(n)
n=s.index('o')
print(n)
n=s.index('o',5)
print(n)
# n=s.index('z')
# print(n)

s="this is a sentence containing few words"
k=s.split()
print(k)

s="hello world"
r=s.isupper()
print(r)
r=s.islower()
print(r)

# format()
name = "ARJUN"
favourite_color = "Navy Blue"
sentence = "{}'s favourite color is {}"
print(sentence)
r=sentence.format(favourite_color,name)
print(r)
# print(sentence.format(name.capitalize(),favourite_color))
sentence = "{}'s favourite color is {}".format(name,favourite_color)
print(sentence)

# f-strings
sentence = f"{name}'s favourite color is {favourite_color}"
# sentence = f"{name.lower()}'s favourite {3+4} color is {favourite_color}"
print(sentence)
help(str.lower)
# print(dir(str))


# data types
# data structures - list, tuple, set, dictionary

# LIST
# list is a mutable ordered sequence of elements
l=[1,2,3,4,5,6.0,"hi",True]
print(l)
print(type(l))

# accessing
e=l[2]
print(e)
e=l[6]
print(e)

# len()
n=len(l)
print(n)

s="hello world"
n=len(s)
print(n)
i=l[:5]
print(i)

# modifying a list
print(l[1])
l[1]=10
print(l)

marks=[89,90,58,70,85]

# list functions
# sum(), min(), max(), len(), join()
# sm=marks[0]+marks[1]+
sm=sum(marks)
l=len(marks)
print(sm/l)
print(max(marks))
print(min(marks))

lw=['this', 'is', 'a', 'sentence', 'containing', 'few', 'words']
s=" ".join(lw)
print(s)

# membership operators
# in, not in
marks=[89,90,58,70,70,85]
r=70 in marks
print(70 in marks)
print(71 in marks)
print(71 not in marks)

marks[1]=80

# list methods
# vn.method_name([arg1[,arg2,]])
marks.append(67)
print(marks)
marks.insert(2,94)
print(marks)
print(dir(list))
# v=marks.pop(0)
v=marks.pop()
print(v,marks)
marks.remove(70)
print(marks)
el=[]
marks.reverse()
print(marks)



# exercise 6
# print true if a 'number' is even

# intialize it with number of your choice
number = 49
print(number%2==0)
# 1%2=1
# 2%2=0
# 3%2=1
# 4%2=0
# 5%2=1
# 6%2=0
# 7%2=1

print(dir(list))

# TUPLE
# list is a immutable ordered sequence of elements
#They are similar to lists in the way they are created and accessed.
# Tuples are created using parenthesis - ()
# Tuples are mainly used when you have values which are closely related and their position matters
t=(1,2,3,4,5)
t2=()
t3=1,2,3,4,5
print(t,t2,t3)
print(type(t))
print(t[1])
print(dir(tuple))
print(t.index(2))
# print(t.index(20))

#SET
# Set is a mutable unordered collection of unique elements
# Set is created using curly braces - {}
s={1,2,3,4,5,1,2,3}
s2=set()
print(s)
print(type(s))
s.add(6)
print(s)
print(dir(set))
s.remove(1)
print(s)
help(set.pop)
fav_actors = ["Prabhas","Shruthi Haasan","Naani","Ram Charan","Prabhas","Nivedha Thomas","Naani",
                   "Ram Charan","Rakul Preeth","Samantha","Rakul Preeth","Prabhas","Samantha",
                  "Nivedha Thomas","Naaga chaithanya","Salman khan","Salman khan","Vijay","Shradha kapoor","Vijay",
                  "Shruthi Haasan","Naani","Ram Charan","Prabhas","Nivedha Thomas","Naaga chaithanya","Salman khan"]

print(len(fav_actors))
# type conversion functions
# list(), tuple(), set()
fa=set(fav_actors)
print(len(fa))
fal=list(fa)
print(fal)

# s1={}
# s2={}
# s3=s1.union(s2)
# s4=s1.intersection(s2)

# print(s1.issubset(s3))
# print(s3.issuperset(s1))


# IDENTITY OPERATORS
# is, is not

# literal
# literal pool
a=1
b=1
c=2
d=c
e="hi"
f="hi"
print(a is b)
print(a is c)
print(a is not c)

l=[1,2,3,4,5]
l2=[1,2,3,4,5]
print(l is l2)
l3=l
print(l is l3)
l.append(6)
print(l3)


# DICTIONARY
std={"name":"sam","age":20,"rollno":1252,"class":9}
# std={"name":"sam","age":20,"rollno":1252,"class":9,"class":10}

print(std)
print(type(std))

# accessing
print(std["name"])
print(std["rollno"])

#update/modify
std["rollno"]=1250
print(std)
print("name" in std)
print(1250 in std)

# adding a new key value pair
std["section"]='A'
print(std)
print(dir(dict))

std.update({"address":"uppal"})
print(std)

print(std.values())
print(std.keys())
print(std.items())

l=[1,2,3,4,[10,20,30]]
print(l[4][2])

v=list(std.values())
print(v)

# get()
print(std["name"])
# print(std["marks"]) #error
print(std.get("name"))
print(std.get("name","Name not available"))
print(std.get("marks"))
print(std.get("marks","Not available"))


# nested dicitionary
std={"name":"sam",
     "age":20,
     "rollno":1252,
     "class":9,
     "address":{"hno":"2-2-10","area":"nehru nagar","town":"hyd","pincode":500013}
     }
print(std["address"]["pincode"])

students=[{"name":"sam","age":20},{"name":"hari","age":21},{"name":"raj","age":22}]
print(students[2])
print(students[2]["age"])
