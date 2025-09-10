import random

def updategamedata(name,turns):
  f=open("gamedata.txt","a")
  f.write(f"{name},{turns}\n")
  f.close()

def printleaderboard():
  f=open("gamedata.txt","r")
  data=f.readlines()
  t=lambda x:int(x.split(",")[1])
  data.sort(key=t)
  print("Leaderboard:")
  rank=1
# 1. mahesh     7
  for nt in data:
    nt=nt.split(',')   #["mahesh","70\n"]
    print(f"{rank}. {nt[0]}\t\t\t{nt[1]}",end="")
    rank+=1


r=random.randrange(1,101) #50
name=input("Enter your name:")
turns=0

while True:
  useri=int(input("Guess the number(1-100):"))
  turns+=1
  if useri==r:
    print("You guessed right!!")
    print(f"You took {turns} turns to guess right.")
    break
  elif r>useri:
    print("Given number is larger. Try again")
  elif r<useri:
    print("Given number is smaller. Try again")

updategamedata(name,turns)
printleaderboard()
