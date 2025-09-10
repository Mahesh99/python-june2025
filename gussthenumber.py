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

