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

# list
# list methods
# append, pop, remove, insert, 

# tuple
t=(1,2,3,4)
dimens = 10,20,15
print(dimens[1])
print(t[3])
marks=[10,20,15,17,18]

s={7,8,10,1,1,2,3,4,4,5}
print(s)

fav_actors = ["Prabhas","Shruthi Haasan","Naani","Ram Charan","Prabhas","Nivedha Thomas","Naani",
                   "Ram Charan","Rakul Preeth","Samantha","Rakul Preeth","Prabhas","Samantha",
                  "Nivedha Thomas","Naaga chaithanya","Salman khan","Salman khan","Vijay","Shradha kapoor","Vijay",
                  "Shruthi Haasan","Naani","Ram Charan","Prabhas","Nivedha Thomas","Naaga chaithanya","Salman khan"]
print(len(fav_actors))
fas=set(fav_actors)
print(fas)
print(len(fas))
favlist=list(fas)
print(favlist)

# list(), tuple(), set()
# int(), float(), str()

# set methods
# union(), intersection(), issuperset(), issubset()
a={1,1,2,3,4}
b={3,4,5,6}
c={1,2,3}
print(a.union(b))
print(a.intersection(b))
print(c.issubset(a))
print(a.issuperset(c))

# dictionary
d={'a':1,'b':2,'c':3}
print(len(d))
print(d['c'])
d['c']=4
print(d)

el=[]
et=()
es=set()
ed={}
print(type(ed),type(es))

marks=[10,20,15,17,18]
print(10 in marks)
print(1 not in marks)

print(1 in d)
print('a' in d)

print()
a=1
b=1
c=2
d=2
e='hi'
f='hello'
g=f
print(g is f)
print(g is not f)
l=[1,2,3,4]
k=[1,2,3,4]
print(l is k)
n=k
k.append(5)
print(n)
z=k.copy()
print(z is k)

d={'a':1,'b':2}
print(d.keys())
print(d.values())
print(d.items())
keys=list(d.keys())
print(keys)
d['d']=5
d.update({'e':6,'f':7})
print(d)

# print(d['c'])
print(d.get('c'))
print(d.get('c',100))
# None is a keyword
# used to represent nothing

class_marks = {
    "Arun":{
        "Hindi":78,
        "English":89,
        "Maths":90,
        "Science":90
    },
    "Smitha":{
        "Hindi":56,
        "English":80,
        "Maths":92,
        "Science":94
    },
    "Naveen":{
        "Hindi":80,
        "English":89,
        "Maths":90,
        "Science":90
    }
}
print(class_marks['Naveen']['English'])
print(class_marks['Smitha']['Maths'])

employees = [{
                "name":"Sravan",
                "age":25,
                "salary":30000
             },
             {
                "name":"Rahul",
                "age":27,
                "salary":32000
             },
             {
                "name":"Keerthana",
                "age":23,
                "salary":35000
             }
            ]
print(employees[1])
print(employees[1]['salary'])