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