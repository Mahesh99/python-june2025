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
advice = "It's always good to follow best practices"
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
print(s[5])
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
j="welcome to pramanicus"

v=j[3:10:3] #"come to"
print(v)
