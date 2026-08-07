# This a guess the number game 
# You have 10 tries
import random
x=random.randint(1,100)
y=0
while y <10 :
    guess = int(input("Whats your guess ?"))
    if x == guess:
            print("Great guess")
            break
    elif guess >x:
            print("Guess is higher than the number")
    elif guess < x:
            print("Guess is lower than the number")   

    y = y+1
else:
       print("you are out of chances")  
