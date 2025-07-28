my_num=8
if my_num<0 :
    print(my_num)
else:
    print("FALSE")

print("hello")
print()




rating = "Excellent"
points = 10

if rating == "Excellent":
    points += 5
elif rating == "Good":
    points += 4
elif rating == "Average":
    points += 3
elif rating == "Fair":
    points += 2
else:
    points += 1
print("Your updated points: {}!".format(points))
print()
#nested if


a = 15
if a%3 == 0:
    if a%5 == 0:
        print(str(a),"is a multiple of 3 and 5")
else:
    print("Not a multiple of 3 and 5")




numbers = [1,2,3,5,7,8]
# example 1
for n in numbers:
    print(n**2,n**3)